"""
Ryan Rozema
mypl_ast.py
HW5
"""
class ASTNode(object):
    """The base class for the abstract syntax tree."""

    def accept(self, visitor): pass


class Stmt(ASTNode):
    """The base class for all statement nodes."""

    def accept(self, visitor): pass


class Expr(ASTNode):
    """The base class for all expression nodes."""

    def accept(self, visitor): pass


class BoolExpr(ASTNode):
    """The base class for Boolean (expression) nodes."""

    def accept(self, visitor): pass


class SimpleBoolExpr(BoolExpr):
    """A simple boolean expression consists of a single expression,
    possibly negated.
    """

    def __init__(self):
        self.expr = None  # Expr node
        self.negated = False

    def accept(self, visitor):
        visitor.visit_simple_bool_expr(self)


class ComplexBoolExpr(BoolExpr):
    """A complex boolean expression consists of an expression, a Boolean
    relation (==, <=, !=, etc.), another expression, and possibly an
    'and' or 'or' followed by additional boolean expressions. An
    entire complex boolean expression can also be negated.
    """

    def __init__(self):
        super(ComplexBoolExpr, self).__init__()
        self.negated = False
        self.first_expr = None  # Expr node
        self.bool_rel = None  # Token (==, <=, !=, etc.)
        self.second_expr = None  # Expr node
        self.has_bool_connector = False  # true if has an AND or OR
        self.bool_connector = None  # Token (AND or OR)
        self.rest = None  # Expr node

    def accept(self, visitor):
        visitor.visit_complex_bool_expr(self)


class StmtList(ASTNode):
    """A statement list consists of a list of statements."""

    def __init__(self):
        self.stmts = []  # list of Stmt

    def accept(self, visitor):
        visitor.visit_stmt_list(self)


class BasicIf(object):
    """A basic if holds a condition (Boolean expression) and a list of
    statements (the body of the if).
    """

    def __init__(self):
        self.bool_expr = None  # BoolExpr node
        self.stmt_list = StmtList()


class IfStmt(Stmt):
    """An if stmt consists of a basic if part, a (possibly empty) list of
    else ifs, and an optional else part (represented as a statement
    list).
    """

    def __init__(self):
        self.if_part = BasicIf()
        self.elseifs = []  # list of BasicIf
        self.has_else = False
        self.else_stmts = StmtList()

    def accept(self, visitor):
        visitor.visit_if_stmt(self)


class WhileStmt(Stmt):
    """A while statement consists of a condition (Boolean expression) and
    a statement list (the body of the while).
    """

    def __init__(self):
        self.bool_expr = None  # a BoolExpr node
        self.stmt_list = StmtList()

    def accept(self, visitor):
        visitor.visit_while_stmt(self)


class PrintStmt(Stmt):
    """A print statement consists of a expression to print."""

    def __init__(self):
        self.expr = None  # an Expr node
        self.is_println = False

    def accept(self, visitor):
        visitor.visit_print_stmt(self)


class AssignStmt(Stmt):
    """An assignment statement consists of an identifier (possibly
    indexed), and an expression.
    """

    def __init__(self):
        self.lhs = None  # Token (ID)
        self.index_expr = None  # Expr node
        self.rhs = None  # Expr node

    def accept(self, visitor):
        visitor.visit_assign_stmt(self)


class SimpleExpr(Expr):
    """A simple expression consists of a value or identifier."""

    def __init__(self):
        self.term = None  # Token

    def accept(self, visitor):
        visitor.visit_simple_expr(self)


class IndexExpr(Expr):
    """An index expression consists of an identifier and an expression."""

    def __init__(self):
        self.identifier = None  # Token (ID)
        self.expr = None  # Expr node

    def accept(self, visitor):
        visitor.visit_index_expr(self)


class ListExpr(Expr):
    """A list expression consists of a list of elements (expressions)."""

    def __init__(self):
        super(ListExpr, self).__init__()
        self.expressions = []  # list of Expr nodes

    def accept(self, visitor):
        visitor.visit_list_expr(self)


class ReadExpr(Expr):
    """A read expression consists of a message string."""

    def __init__(self):
        self.msg = None  # str
        self.is_read_int = False

    def accept(self, visitor):
        visitor.visit_read_expr(self)


class ComplexExpr(Expr):
    """A complex expression consist of an expression, followed by a
    mathematical operator (+, -, *, etc.), followed by another
    (possibly complex) expression.
    """

    def __init__(self):
        self.first_operand = None  # Expr node
        self.math_rel = None  # Token (+, -, *, etc.)
        self.rest = None  # Expr node

    def accept(self, visitor):
        visitor.visit_complex_expr(self)


class Visitor(object):
    """The base class for AST visitors."""

    def visit_stmt_list(self, stmt_list): pass

    def visit_simple_bool_expr(self, simple_bool_expr): pass

    def visit_complex_bool_expr(self, complex_bool_expr): pass

    def visit_if_stmt(self, if_stmt): pass

    def visit_while_stmt(self, while_stmt): pass

    def visit_print_stmt(self, print_stmt): pass

    def visit_assign_stmt(self, assign_stmt): pass

    def visit_simple_expr(self, simple_expr): pass

    def visit_index_expr(self, index_expr): pass

    def visit_list_expr(self, list_expr): pass

    def visit_read_expr(self, read_expr): pass

    def visit_complex_expr(self, complex_expr): pass
