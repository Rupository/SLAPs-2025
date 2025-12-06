import sys
import json
from antlr4 import *
from dfyPyParse.dafnyLexer import dafnyLexer
from dfyPyParse.dafnyParser import dafnyParser
from dfyPyParse.dafnyVisitor import dafnyVisitor

class DafnyJSONVisitor(dafnyVisitor):
    def __init__(self):
        self.methods = []
        self.current_method = None

    def visitProgram(self, ctx: dafnyParser.ProgramContext):
        self.visitChildren(ctx)
        return self.methods

    def visitMethodDecl(self, ctx: dafnyParser.MethodDeclContext):
        sig = ctx.methodSignatureDecl()
        # Handle cases where method name is a normal identifier or an uppercase one
        method_name = sig.identifier().getText() if sig.identifier() else sig.upperIdentifier().getText()
        
        self.current_method = {
            "method_name": method_name,
            "loops": [],
            "preconditions": [],
            "postconditions": [],
            "parameters": [],
            "returns": []
        }

        # 1. Parameters
        if sig.parameters():
            # The first set of parameters are inputs
            self.current_method["parameters"] = self.extract_params(sig.parameters(0))

        # 2. Returns
        # If there is a second set of parameters, they are the return values
        if len(sig.parameters()) > 1:
            self.current_method["returns"] = self.extract_params(sig.parameters(1))

        # 3. Pre/Post Conditions
        for note in sig.verifierAnnotation():
            if note.requires():
                self.current_method["preconditions"].append(note.requires().expression().getText())
            elif note.ensures():
                self.current_method["postconditions"].append(note.ensures().expression().getText())

        # 4. Visit Body
        if ctx.sequence():
            self.visit(ctx.sequence())

        self.methods.append(self.current_method)
        self.current_method = None
        return

    def extract_params(self, params_ctx):
        results = []
        if not params_ctx.identifierType():
            return results
        for p in params_ctx.identifierType():
            results.append({
                "name": p.identifier().getText(), 
                "type": p.type_().getText()
            })
        return results

    # -------------------------------------------------------------------------
    # LOOP HANDLING
    # -------------------------------------------------------------------------

    def visitWhileStatement(self, ctx: dafnyParser.WhileStatementContext):
        if self.current_method is None: return

        invariants = []
        if ctx.verifierAnnotation():
            for note in ctx.verifierAnnotation():
                if note.invariant():
                    invariants.append(note.invariant().expression().getText())

        # Analyze variables used in the loop body
        variables = self.analyze_loop_variables(ctx, ctx.sequence())

        loop_obj = {
            "type": "while",
            "condition": ctx.expression().getText(),
            "variables": variables,
            "invariants": invariants
        }
        self.current_method["loops"].append(loop_obj)

    def visitForLoop(self, ctx: dafnyParser.ForLoopContext):
        if self.current_method is None: return

        invariants = []
        # Checks for invariants if grammar allows them
        if hasattr(ctx, 'verifierAnnotation') and ctx.verifierAnnotation():
             for note in ctx.verifierAnnotation():
                if note.invariant():
                    invariants.append(note.invariant().expression().getText())

        loop_var = ctx.identifier().getText()
        start_expr = ctx.expression(0).getText()
        end_expr = ctx.expression(1).getText()
        
        # Analyze other variables in the body
        variables = self.analyze_loop_variables(ctx, ctx.sequence())
        
        # Add the loop counter explicitly
        variables.insert(0, {
            "name": loop_var,
            "type": "int",
            "initially": start_expr,
            "assignment": f"{loop_var} + 1"
        })

        loop_obj = {
            "type": "for",
            "condition": f"{loop_var} < {end_expr}",
            "variables": variables,
            "invariants": invariants
        }
        self.current_method["loops"].append(loop_obj)

    # -------------------------------------------------------------------------
    # LOOK-UP HELPERS
    # -------------------------------------------------------------------------

    def analyze_loop_variables(self, loop_ctx, body_sequence):
        """
        1. Find assignments inside the loop.
        2. Look UP the tree to find where those variables were initialized.
        """
        updates = self.scan_for_updates(body_sequence)
        results = []

        for var_name, assignment_expr in updates.items():
            initial_val = self.find_initial_value(loop_ctx, var_name)
            
            results.append({
                "name": var_name,
                "type": "int", # Defaulting to int as type inference is hard
                "initially": initial_val,
                "assignment": assignment_expr
            })
        return results

    def find_initial_value(self, start_node, var_name):
        """
        Walks backwards up the AST.
        """
        node = start_node
        while node.parentCtx is not None:
            parent = node.parentCtx
            
            # If we are in a block (Sequence), look at previous statements
            if isinstance(parent, dafnyParser.SequenceContext):
                for stmt in parent.statement():
                    if stmt is node: 
                        break # Stop when we reach the current block
                    
                    # Check Declarations: var x := 10;
                    if stmt.declaration():
                        decl = stmt.declaration()
                        lhs_list = decl.declarationLhs().declAssignLhs()
                        rhs_list = decl.declAssignRhs()
                        
                        # Handle multiple declarations: var x, y := 1, 2;
                        if isinstance(lhs_list, list):
                            for i, lhs in enumerate(lhs_list):
                                if lhs.getText() == var_name:
                                    # Safe access if rhs is list or single
                                    if isinstance(rhs_list, list) and i < len(rhs_list):
                                        return rhs_list[i].getText()
                                    return rhs_list.getText() if not isinstance(rhs_list, list) else "unknown"
                        elif lhs_list.getText() == var_name:
                             return rhs_list.getText()

                    # Check Assignments: x := 10;
                    if stmt.assignment():
                        assign = stmt.assignment()
                        lhs_list = assign.assignmentLhs()
                        rhs_list = assign.declAssignRhs()
                        for i, lhs in enumerate(lhs_list):
                            if lhs.getText() == var_name:
                                if isinstance(rhs_list, list) and i < len(rhs_list):
                                    return rhs_list[i].getText()
                                return rhs_list.getText()

            node = parent

        # Check Method Parameters if not found in body
        for param in self.current_method["parameters"]:
            if param["name"] == var_name:
                return f"(parameter {var_name})"

        return "unknown"

    def scan_for_updates(self, sequence_ctx):
        """ Scans a loop body for variables being updated. """
        updates = {}
        if not sequence_ctx or not sequence_ctx.statement(): 
            return updates

        for stmt in sequence_ctx.statement():
            if stmt.assignment():
                assign = stmt.assignment()
                lhs_list = assign.assignmentLhs()
                rhs_list = assign.declAssignRhs()
                
                for i, lhs in enumerate(lhs_list):
                    var_name = lhs.getText()
                    # Simplified: just grabs text of right-hand side
                    rhs_expr = "unknown"
                    if isinstance(rhs_list, list) and i < len(rhs_list):
                        rhs_expr = rhs_list[i].getText()
                    elif not isinstance(rhs_list, list):
                        rhs_expr = rhs_list.getText()
                        
                    updates[var_name] = rhs_expr
        return updates

def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = dafnyLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = dafnyParser(stream)
    tree = parser.program()

    visitor = DafnyJSONVisitor()
    methods_data = visitor.visit(tree)

    print(json.dumps(methods_data, indent=2))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        print("Usage: python dafny_to_json.py <file.dfy>")