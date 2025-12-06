# Generated from dafny.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .dafnyParser import dafnyParser
else:
    from dafnyParser import dafnyParser

# This class defines a complete generic visitor for a parse tree produced by dafnyParser.

class dafnyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by dafnyParser#boolLiteral.
    def visitBoolLiteral(self, ctx:dafnyParser.BoolLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#intLiteral.
    def visitIntLiteral(self, ctx:dafnyParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#realLiteral.
    def visitRealLiteral(self, ctx:dafnyParser.RealLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#charLiteral.
    def visitCharLiteral(self, ctx:dafnyParser.CharLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#stringToken.
    def visitStringToken(self, ctx:dafnyParser.StringTokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#unaryOperator.
    def visitUnaryOperator(self, ctx:dafnyParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#upperIdentifier.
    def visitUpperIdentifier(self, ctx:dafnyParser.UpperIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#identifier.
    def visitIdentifier(self, ctx:dafnyParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#topDecl.
    def visitTopDecl(self, ctx:dafnyParser.TopDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#genericInstantiation.
    def visitGenericInstantiation(self, ctx:dafnyParser.GenericInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#type.
    def visitType(self, ctx:dafnyParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#arrayType.
    def visitArrayType(self, ctx:dafnyParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#mapType.
    def visitMapType(self, ctx:dafnyParser.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#setType.
    def visitSetType(self, ctx:dafnyParser.SetTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#multisetType.
    def visitMultisetType(self, ctx:dafnyParser.MultisetTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#sequenceType.
    def visitSequenceType(self, ctx:dafnyParser.SequenceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#datatypeDecl.
    def visitDatatypeDecl(self, ctx:dafnyParser.DatatypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#datatypeConstructor.
    def visitDatatypeConstructor(self, ctx:dafnyParser.DatatypeConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#classDecl.
    def visitClassDecl(self, ctx:dafnyParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#classMemberDecl.
    def visitClassMemberDecl(self, ctx:dafnyParser.ClassMemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#traitDecl.
    def visitTraitDecl(self, ctx:dafnyParser.TraitDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#traitMemberDecl.
    def visitTraitMemberDecl(self, ctx:dafnyParser.TraitMemberDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#functionSignatureDecl.
    def visitFunctionSignatureDecl(self, ctx:dafnyParser.FunctionSignatureDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#methodSignatureDecl.
    def visitMethodSignatureDecl(self, ctx:dafnyParser.MethodSignatureDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#fieldDecl.
    def visitFieldDecl(self, ctx:dafnyParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#identifierType.
    def visitIdentifierType(self, ctx:dafnyParser.IdentifierTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#parameters.
    def visitParameters(self, ctx:dafnyParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#functionDecl.
    def visitFunctionDecl(self, ctx:dafnyParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#methodDecl.
    def visitMethodDecl(self, ctx:dafnyParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#constructorDecl.
    def visitConstructorDecl(self, ctx:dafnyParser.ConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#disj.
    def visitDisj(self, ctx:dafnyParser.DisjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#expression.
    def visitExpression(self, ctx:dafnyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#datatypeFieldUpdate.
    def visitDatatypeFieldUpdate(self, ctx:dafnyParser.DatatypeFieldUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#modulus.
    def visitModulus(self, ctx:dafnyParser.ModulusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#multisetConversion.
    def visitMultisetConversion(self, ctx:dafnyParser.MultisetConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#literal.
    def visitLiteral(self, ctx:dafnyParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#callParameters.
    def visitCallParameters(self, ctx:dafnyParser.CallParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#functionCall.
    def visitFunctionCall(self, ctx:dafnyParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#classInstantiation.
    def visitClassInstantiation(self, ctx:dafnyParser.ClassInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#datatypeInstantiation.
    def visitDatatypeInstantiation(self, ctx:dafnyParser.DatatypeInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#ternaryExpression.
    def visitTernaryExpression(self, ctx:dafnyParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#matchExpression.
    def visitMatchExpression(self, ctx:dafnyParser.MatchExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#caseExpression.
    def visitCaseExpression(self, ctx:dafnyParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#arrayLength.
    def visitArrayLength(self, ctx:dafnyParser.ArrayLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#index.
    def visitIndex(self, ctx:dafnyParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#setDisplay.
    def visitSetDisplay(self, ctx:dafnyParser.SetDisplayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#setComprehension.
    def visitSetComprehension(self, ctx:dafnyParser.SetComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#sequenceDisplay.
    def visitSequenceDisplay(self, ctx:dafnyParser.SequenceDisplayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#sequenceComprehension.
    def visitSequenceComprehension(self, ctx:dafnyParser.SequenceComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#mapConstructor.
    def visitMapConstructor(self, ctx:dafnyParser.MapConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#mapComprehension.
    def visitMapComprehension(self, ctx:dafnyParser.MapComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#indexElem.
    def visitIndexElem(self, ctx:dafnyParser.IndexElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#statement.
    def visitStatement(self, ctx:dafnyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#assertStatement.
    def visitAssertStatement(self, ctx:dafnyParser.AssertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#breakStatement.
    def visitBreakStatement(self, ctx:dafnyParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#continueStatement.
    def visitContinueStatement(self, ctx:dafnyParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#declIdentifier.
    def visitDeclIdentifier(self, ctx:dafnyParser.DeclIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#declAssignLhs.
    def visitDeclAssignLhs(self, ctx:dafnyParser.DeclAssignLhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#declAssignRhs.
    def visitDeclAssignRhs(self, ctx:dafnyParser.DeclAssignRhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#declarationLhs.
    def visitDeclarationLhs(self, ctx:dafnyParser.DeclarationLhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#declaration.
    def visitDeclaration(self, ctx:dafnyParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#assignmentLhs.
    def visitAssignmentLhs(self, ctx:dafnyParser.AssignmentLhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#assignment.
    def visitAssignment(self, ctx:dafnyParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#print.
    def visitPrint(self, ctx:dafnyParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#voidMethodCall.
    def visitVoidMethodCall(self, ctx:dafnyParser.VoidMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#sequence.
    def visitSequence(self, ctx:dafnyParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#matchStatement.
    def visitMatchStatement(self, ctx:dafnyParser.MatchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#caseStatement.
    def visitCaseStatement(self, ctx:dafnyParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#ifStatement.
    def visitIfStatement(self, ctx:dafnyParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#forallStatement.
    def visitForallStatement(self, ctx:dafnyParser.ForallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#forLoop.
    def visitForLoop(self, ctx:dafnyParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#whileStatement.
    def visitWhileStatement(self, ctx:dafnyParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#verifierAnnotation.
    def visitVerifierAnnotation(self, ctx:dafnyParser.VerifierAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#decreases.
    def visitDecreases(self, ctx:dafnyParser.DecreasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#ensures.
    def visitEnsures(self, ctx:dafnyParser.EnsuresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#invariant.
    def visitInvariant(self, ctx:dafnyParser.InvariantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#modifies.
    def visitModifies(self, ctx:dafnyParser.ModifiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#reads.
    def visitReads(self, ctx:dafnyParser.ReadsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#requires.
    def visitRequires(self, ctx:dafnyParser.RequiresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#arrayConstructor.
    def visitArrayConstructor(self, ctx:dafnyParser.ArrayConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#arrayComprehension.
    def visitArrayComprehension(self, ctx:dafnyParser.ArrayComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#arrayValues.
    def visitArrayValues(self, ctx:dafnyParser.ArrayValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#topDeclMember.
    def visitTopDeclMember(self, ctx:dafnyParser.TopDeclMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dafnyParser#program.
    def visitProgram(self, ctx:dafnyParser.ProgramContext):
        return self.visitChildren(ctx)



del dafnyParser