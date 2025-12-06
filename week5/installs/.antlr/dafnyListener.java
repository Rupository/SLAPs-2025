// Generated from c:/Users/Tintu/Documents/Obsidian/Notes/Academics/Ashoka/Semester 5/SLAPs/Code/SLAPs-2025/week5/installs/dafny.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link dafnyParser}.
 */
public interface dafnyListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link dafnyParser#boolLiteral}.
	 * @param ctx the parse tree
	 */
	void enterBoolLiteral(dafnyParser.BoolLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#boolLiteral}.
	 * @param ctx the parse tree
	 */
	void exitBoolLiteral(dafnyParser.BoolLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#intLiteral}.
	 * @param ctx the parse tree
	 */
	void enterIntLiteral(dafnyParser.IntLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#intLiteral}.
	 * @param ctx the parse tree
	 */
	void exitIntLiteral(dafnyParser.IntLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#realLiteral}.
	 * @param ctx the parse tree
	 */
	void enterRealLiteral(dafnyParser.RealLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#realLiteral}.
	 * @param ctx the parse tree
	 */
	void exitRealLiteral(dafnyParser.RealLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#charLiteral}.
	 * @param ctx the parse tree
	 */
	void enterCharLiteral(dafnyParser.CharLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#charLiteral}.
	 * @param ctx the parse tree
	 */
	void exitCharLiteral(dafnyParser.CharLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#stringToken}.
	 * @param ctx the parse tree
	 */
	void enterStringToken(dafnyParser.StringTokenContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#stringToken}.
	 * @param ctx the parse tree
	 */
	void exitStringToken(dafnyParser.StringTokenContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#unaryOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnaryOperator(dafnyParser.UnaryOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#unaryOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnaryOperator(dafnyParser.UnaryOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#upperIdentifier}.
	 * @param ctx the parse tree
	 */
	void enterUpperIdentifier(dafnyParser.UpperIdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#upperIdentifier}.
	 * @param ctx the parse tree
	 */
	void exitUpperIdentifier(dafnyParser.UpperIdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(dafnyParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(dafnyParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#topDecl}.
	 * @param ctx the parse tree
	 */
	void enterTopDecl(dafnyParser.TopDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#topDecl}.
	 * @param ctx the parse tree
	 */
	void exitTopDecl(dafnyParser.TopDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#genericInstantiation}.
	 * @param ctx the parse tree
	 */
	void enterGenericInstantiation(dafnyParser.GenericInstantiationContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#genericInstantiation}.
	 * @param ctx the parse tree
	 */
	void exitGenericInstantiation(dafnyParser.GenericInstantiationContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(dafnyParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(dafnyParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#arrayType}.
	 * @param ctx the parse tree
	 */
	void enterArrayType(dafnyParser.ArrayTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#arrayType}.
	 * @param ctx the parse tree
	 */
	void exitArrayType(dafnyParser.ArrayTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#mapType}.
	 * @param ctx the parse tree
	 */
	void enterMapType(dafnyParser.MapTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#mapType}.
	 * @param ctx the parse tree
	 */
	void exitMapType(dafnyParser.MapTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#setType}.
	 * @param ctx the parse tree
	 */
	void enterSetType(dafnyParser.SetTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#setType}.
	 * @param ctx the parse tree
	 */
	void exitSetType(dafnyParser.SetTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#multisetType}.
	 * @param ctx the parse tree
	 */
	void enterMultisetType(dafnyParser.MultisetTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#multisetType}.
	 * @param ctx the parse tree
	 */
	void exitMultisetType(dafnyParser.MultisetTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#sequenceType}.
	 * @param ctx the parse tree
	 */
	void enterSequenceType(dafnyParser.SequenceTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#sequenceType}.
	 * @param ctx the parse tree
	 */
	void exitSequenceType(dafnyParser.SequenceTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#datatypeDecl}.
	 * @param ctx the parse tree
	 */
	void enterDatatypeDecl(dafnyParser.DatatypeDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#datatypeDecl}.
	 * @param ctx the parse tree
	 */
	void exitDatatypeDecl(dafnyParser.DatatypeDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#datatypeConstructor}.
	 * @param ctx the parse tree
	 */
	void enterDatatypeConstructor(dafnyParser.DatatypeConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#datatypeConstructor}.
	 * @param ctx the parse tree
	 */
	void exitDatatypeConstructor(dafnyParser.DatatypeConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void enterClassDecl(dafnyParser.ClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#classDecl}.
	 * @param ctx the parse tree
	 */
	void exitClassDecl(dafnyParser.ClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#classMemberDecl}.
	 * @param ctx the parse tree
	 */
	void enterClassMemberDecl(dafnyParser.ClassMemberDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#classMemberDecl}.
	 * @param ctx the parse tree
	 */
	void exitClassMemberDecl(dafnyParser.ClassMemberDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#traitDecl}.
	 * @param ctx the parse tree
	 */
	void enterTraitDecl(dafnyParser.TraitDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#traitDecl}.
	 * @param ctx the parse tree
	 */
	void exitTraitDecl(dafnyParser.TraitDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#traitMemberDecl}.
	 * @param ctx the parse tree
	 */
	void enterTraitMemberDecl(dafnyParser.TraitMemberDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#traitMemberDecl}.
	 * @param ctx the parse tree
	 */
	void exitTraitMemberDecl(dafnyParser.TraitMemberDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#functionSignatureDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionSignatureDecl(dafnyParser.FunctionSignatureDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#functionSignatureDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionSignatureDecl(dafnyParser.FunctionSignatureDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#methodSignatureDecl}.
	 * @param ctx the parse tree
	 */
	void enterMethodSignatureDecl(dafnyParser.MethodSignatureDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#methodSignatureDecl}.
	 * @param ctx the parse tree
	 */
	void exitMethodSignatureDecl(dafnyParser.MethodSignatureDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#fieldDecl}.
	 * @param ctx the parse tree
	 */
	void enterFieldDecl(dafnyParser.FieldDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#fieldDecl}.
	 * @param ctx the parse tree
	 */
	void exitFieldDecl(dafnyParser.FieldDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#identifierType}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierType(dafnyParser.IdentifierTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#identifierType}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierType(dafnyParser.IdentifierTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(dafnyParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(dafnyParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(dafnyParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(dafnyParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void enterMethodDecl(dafnyParser.MethodDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#methodDecl}.
	 * @param ctx the parse tree
	 */
	void exitMethodDecl(dafnyParser.MethodDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#constructorDecl}.
	 * @param ctx the parse tree
	 */
	void enterConstructorDecl(dafnyParser.ConstructorDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#constructorDecl}.
	 * @param ctx the parse tree
	 */
	void exitConstructorDecl(dafnyParser.ConstructorDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#disj}.
	 * @param ctx the parse tree
	 */
	void enterDisj(dafnyParser.DisjContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#disj}.
	 * @param ctx the parse tree
	 */
	void exitDisj(dafnyParser.DisjContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(dafnyParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(dafnyParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#datatypeFieldUpdate}.
	 * @param ctx the parse tree
	 */
	void enterDatatypeFieldUpdate(dafnyParser.DatatypeFieldUpdateContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#datatypeFieldUpdate}.
	 * @param ctx the parse tree
	 */
	void exitDatatypeFieldUpdate(dafnyParser.DatatypeFieldUpdateContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#modulus}.
	 * @param ctx the parse tree
	 */
	void enterModulus(dafnyParser.ModulusContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#modulus}.
	 * @param ctx the parse tree
	 */
	void exitModulus(dafnyParser.ModulusContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#multisetConversion}.
	 * @param ctx the parse tree
	 */
	void enterMultisetConversion(dafnyParser.MultisetConversionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#multisetConversion}.
	 * @param ctx the parse tree
	 */
	void exitMultisetConversion(dafnyParser.MultisetConversionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(dafnyParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(dafnyParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#callParameters}.
	 * @param ctx the parse tree
	 */
	void enterCallParameters(dafnyParser.CallParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#callParameters}.
	 * @param ctx the parse tree
	 */
	void exitCallParameters(dafnyParser.CallParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(dafnyParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(dafnyParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#classInstantiation}.
	 * @param ctx the parse tree
	 */
	void enterClassInstantiation(dafnyParser.ClassInstantiationContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#classInstantiation}.
	 * @param ctx the parse tree
	 */
	void exitClassInstantiation(dafnyParser.ClassInstantiationContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#datatypeInstantiation}.
	 * @param ctx the parse tree
	 */
	void enterDatatypeInstantiation(dafnyParser.DatatypeInstantiationContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#datatypeInstantiation}.
	 * @param ctx the parse tree
	 */
	void exitDatatypeInstantiation(dafnyParser.DatatypeInstantiationContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#ternaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterTernaryExpression(dafnyParser.TernaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#ternaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitTernaryExpression(dafnyParser.TernaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#matchExpression}.
	 * @param ctx the parse tree
	 */
	void enterMatchExpression(dafnyParser.MatchExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#matchExpression}.
	 * @param ctx the parse tree
	 */
	void exitMatchExpression(dafnyParser.MatchExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#caseExpression}.
	 * @param ctx the parse tree
	 */
	void enterCaseExpression(dafnyParser.CaseExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#caseExpression}.
	 * @param ctx the parse tree
	 */
	void exitCaseExpression(dafnyParser.CaseExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#arrayLength}.
	 * @param ctx the parse tree
	 */
	void enterArrayLength(dafnyParser.ArrayLengthContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#arrayLength}.
	 * @param ctx the parse tree
	 */
	void exitArrayLength(dafnyParser.ArrayLengthContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#index}.
	 * @param ctx the parse tree
	 */
	void enterIndex(dafnyParser.IndexContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#index}.
	 * @param ctx the parse tree
	 */
	void exitIndex(dafnyParser.IndexContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#setDisplay}.
	 * @param ctx the parse tree
	 */
	void enterSetDisplay(dafnyParser.SetDisplayContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#setDisplay}.
	 * @param ctx the parse tree
	 */
	void exitSetDisplay(dafnyParser.SetDisplayContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#setComprehension}.
	 * @param ctx the parse tree
	 */
	void enterSetComprehension(dafnyParser.SetComprehensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#setComprehension}.
	 * @param ctx the parse tree
	 */
	void exitSetComprehension(dafnyParser.SetComprehensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#sequenceDisplay}.
	 * @param ctx the parse tree
	 */
	void enterSequenceDisplay(dafnyParser.SequenceDisplayContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#sequenceDisplay}.
	 * @param ctx the parse tree
	 */
	void exitSequenceDisplay(dafnyParser.SequenceDisplayContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#sequenceComprehension}.
	 * @param ctx the parse tree
	 */
	void enterSequenceComprehension(dafnyParser.SequenceComprehensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#sequenceComprehension}.
	 * @param ctx the parse tree
	 */
	void exitSequenceComprehension(dafnyParser.SequenceComprehensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#mapConstructor}.
	 * @param ctx the parse tree
	 */
	void enterMapConstructor(dafnyParser.MapConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#mapConstructor}.
	 * @param ctx the parse tree
	 */
	void exitMapConstructor(dafnyParser.MapConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#mapComprehension}.
	 * @param ctx the parse tree
	 */
	void enterMapComprehension(dafnyParser.MapComprehensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#mapComprehension}.
	 * @param ctx the parse tree
	 */
	void exitMapComprehension(dafnyParser.MapComprehensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#indexElem}.
	 * @param ctx the parse tree
	 */
	void enterIndexElem(dafnyParser.IndexElemContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#indexElem}.
	 * @param ctx the parse tree
	 */
	void exitIndexElem(dafnyParser.IndexElemContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(dafnyParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(dafnyParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#assertStatement}.
	 * @param ctx the parse tree
	 */
	void enterAssertStatement(dafnyParser.AssertStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#assertStatement}.
	 * @param ctx the parse tree
	 */
	void exitAssertStatement(dafnyParser.AssertStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void enterBreakStatement(dafnyParser.BreakStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#breakStatement}.
	 * @param ctx the parse tree
	 */
	void exitBreakStatement(dafnyParser.BreakStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void enterContinueStatement(dafnyParser.ContinueStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#continueStatement}.
	 * @param ctx the parse tree
	 */
	void exitContinueStatement(dafnyParser.ContinueStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#declIdentifier}.
	 * @param ctx the parse tree
	 */
	void enterDeclIdentifier(dafnyParser.DeclIdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#declIdentifier}.
	 * @param ctx the parse tree
	 */
	void exitDeclIdentifier(dafnyParser.DeclIdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#declAssignLhs}.
	 * @param ctx the parse tree
	 */
	void enterDeclAssignLhs(dafnyParser.DeclAssignLhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#declAssignLhs}.
	 * @param ctx the parse tree
	 */
	void exitDeclAssignLhs(dafnyParser.DeclAssignLhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#declAssignRhs}.
	 * @param ctx the parse tree
	 */
	void enterDeclAssignRhs(dafnyParser.DeclAssignRhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#declAssignRhs}.
	 * @param ctx the parse tree
	 */
	void exitDeclAssignRhs(dafnyParser.DeclAssignRhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#declarationLhs}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationLhs(dafnyParser.DeclarationLhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#declarationLhs}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationLhs(dafnyParser.DeclarationLhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(dafnyParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(dafnyParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#assignmentLhs}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentLhs(dafnyParser.AssignmentLhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#assignmentLhs}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentLhs(dafnyParser.AssignmentLhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(dafnyParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(dafnyParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(dafnyParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(dafnyParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#voidMethodCall}.
	 * @param ctx the parse tree
	 */
	void enterVoidMethodCall(dafnyParser.VoidMethodCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#voidMethodCall}.
	 * @param ctx the parse tree
	 */
	void exitVoidMethodCall(dafnyParser.VoidMethodCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#sequence}.
	 * @param ctx the parse tree
	 */
	void enterSequence(dafnyParser.SequenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#sequence}.
	 * @param ctx the parse tree
	 */
	void exitSequence(dafnyParser.SequenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#matchStatement}.
	 * @param ctx the parse tree
	 */
	void enterMatchStatement(dafnyParser.MatchStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#matchStatement}.
	 * @param ctx the parse tree
	 */
	void exitMatchStatement(dafnyParser.MatchStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#caseStatement}.
	 * @param ctx the parse tree
	 */
	void enterCaseStatement(dafnyParser.CaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#caseStatement}.
	 * @param ctx the parse tree
	 */
	void exitCaseStatement(dafnyParser.CaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(dafnyParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(dafnyParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#forallStatement}.
	 * @param ctx the parse tree
	 */
	void enterForallStatement(dafnyParser.ForallStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#forallStatement}.
	 * @param ctx the parse tree
	 */
	void exitForallStatement(dafnyParser.ForallStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void enterForLoop(dafnyParser.ForLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void exitForLoop(dafnyParser.ForLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(dafnyParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(dafnyParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#verifierAnnotation}.
	 * @param ctx the parse tree
	 */
	void enterVerifierAnnotation(dafnyParser.VerifierAnnotationContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#verifierAnnotation}.
	 * @param ctx the parse tree
	 */
	void exitVerifierAnnotation(dafnyParser.VerifierAnnotationContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#decreases}.
	 * @param ctx the parse tree
	 */
	void enterDecreases(dafnyParser.DecreasesContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#decreases}.
	 * @param ctx the parse tree
	 */
	void exitDecreases(dafnyParser.DecreasesContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#ensures}.
	 * @param ctx the parse tree
	 */
	void enterEnsures(dafnyParser.EnsuresContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#ensures}.
	 * @param ctx the parse tree
	 */
	void exitEnsures(dafnyParser.EnsuresContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#invariant}.
	 * @param ctx the parse tree
	 */
	void enterInvariant(dafnyParser.InvariantContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#invariant}.
	 * @param ctx the parse tree
	 */
	void exitInvariant(dafnyParser.InvariantContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#modifies}.
	 * @param ctx the parse tree
	 */
	void enterModifies(dafnyParser.ModifiesContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#modifies}.
	 * @param ctx the parse tree
	 */
	void exitModifies(dafnyParser.ModifiesContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#reads}.
	 * @param ctx the parse tree
	 */
	void enterReads(dafnyParser.ReadsContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#reads}.
	 * @param ctx the parse tree
	 */
	void exitReads(dafnyParser.ReadsContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#requires}.
	 * @param ctx the parse tree
	 */
	void enterRequires(dafnyParser.RequiresContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#requires}.
	 * @param ctx the parse tree
	 */
	void exitRequires(dafnyParser.RequiresContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#arrayConstructor}.
	 * @param ctx the parse tree
	 */
	void enterArrayConstructor(dafnyParser.ArrayConstructorContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#arrayConstructor}.
	 * @param ctx the parse tree
	 */
	void exitArrayConstructor(dafnyParser.ArrayConstructorContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#arrayComprehension}.
	 * @param ctx the parse tree
	 */
	void enterArrayComprehension(dafnyParser.ArrayComprehensionContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#arrayComprehension}.
	 * @param ctx the parse tree
	 */
	void exitArrayComprehension(dafnyParser.ArrayComprehensionContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#arrayValues}.
	 * @param ctx the parse tree
	 */
	void enterArrayValues(dafnyParser.ArrayValuesContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#arrayValues}.
	 * @param ctx the parse tree
	 */
	void exitArrayValues(dafnyParser.ArrayValuesContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#topDeclMember}.
	 * @param ctx the parse tree
	 */
	void enterTopDeclMember(dafnyParser.TopDeclMemberContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#topDeclMember}.
	 * @param ctx the parse tree
	 */
	void exitTopDeclMember(dafnyParser.TopDeclMemberContext ctx);
	/**
	 * Enter a parse tree produced by {@link dafnyParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(dafnyParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link dafnyParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(dafnyParser.ProgramContext ctx);
}