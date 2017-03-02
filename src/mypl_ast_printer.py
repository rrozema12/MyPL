"""
Ryan Rozema
mypl_ast_printer
hw5
"""
import mypl_ast as ast


class ASTPrintVisitor(ast.Visitor):
    """An AST printer"""

    def __init__(self, output_stream):
        self.indent = 0
        self.output_stream = output_stream

    # helper functions
    def write(self, msg):
        self.output_stream.write(msg)

    def indent_write(self, msg):
        self.write('  ' * self.indent + msg)

    # visitor functions

    def visit_stmt_list(self, stmt_list):
        self.indent_write('StmtList:\n')
        self.indent += 1
        for stmt in stmt_list.stmts:
            stmt.accept(self)
        self.indent -= 1

    def visit_simple_bool_expr(self, simple_bool_expr):
        self.indent_write('SimpleBoolExpr:\n')
        self.indent += 1
        if simple_bool_expr.negated:
            self.indent_write('NOT\n')
        simple_bool_expr.expr.accept(self)
        self.write('\n')
        self.indent -= 1

    def visit_complex_bool_expr(self, complex_bool_expr):
        self.indent_write('ComplexBoolExpr:\n')
        self.indent += 1
        if complex_bool_expr.negated:
            self.indent_write('NOT\n')
        complex_bool_expr.first_expr.accept(self)
        self.indent_write(complex_bool_expr.bool_rel.tokentype)
        self.write('\n')
        complex_bool_expr.second_expr.accept(self)
        if complex_bool_expr.has_bool_connector:
            self.indent_write(complex_bool_expr.bool_connector.tokentype)
            self.write('\n')
            complex_bool_expr.rest.accept(self)
        self.indent -= 1

    def visit_if_stmt(self, if_stmt):
        self.indent_write('IfStmt:\n')
        self.indent += 1
        self.indent_write('IF:\n')
        self.indent += 1
        if_stmt.if_part.bool_expr.accept(self)
        self.indent -= 1
        self.indent_write('THEN:\n')
        self.indent += 1
        if_stmt.if_part.stmt_list.accept(self)
        self.indent -= 1
        for elseif in if_stmt.elseifs:
            self.indent_write('ELSEIF:\n')
            self.indent += 1
            elseif.bool_expr.accept(self)
            self.indent -= 1
            self.indent_write('THEN:\n')
            self.indent += 1
            elseif.stmt_list.accept(self)
            self.indent -= 1
        if if_stmt.has_else:
            self.indent_write('ELSE:\n')
            self.indent += 1
            if_stmt.else_stmts.accept(self)
            self.indent -= 1
        self.indent -= 1

    def visit_while_stmt(self, while_stmt):
        self.indent_write('WhileStmt:\n')
        self.indent += 1
        self.indent_write('CONDITION:\n')
        self.indent += 1
        while_stmt.bool_expr.accept(self)
        self.indent -= 1
        self.indent_write('BODY:\n')
        self.indent += 1
        while_stmt.stmt_list.accept(self)
        self.indent -= 1
        self.indent -= 1

    def visit_print_stmt(self, print_stmt):
        self.indent_write('PrintStmt: ')
        if print_stmt.is_println:
            self.write('PRINTLN\n')
        else:
            self.write('PRINT\n')
        self.indent += 1
        print_stmt.expr.accept(self)
        self.indent -= 1

    def visit_assign_stmt(self, assign_stmt):
        self.indent_write('AssignStmt:\n')
        self.indent += 1
        if assign_stmt.index_expr != None:
            self.indent_write('INDEXED ID: ')
            self.write(assign_stmt.lhs.lexeme + '\n')
            assign_stmt.index_expr.accept(self)
        else:
            self.indent_write('ID: ')
            self.write(assign_stmt.lhs.lexeme + '\n')
        assign_stmt.rhs.accept(self)
        self.indent -= 1

    def visit_simple_expr(self, simple_expr):
        self.indent_write('SimpleExpr: ')
        tokentype = simple_expr.term.tokentype
        lexeme = simple_expr.term.lexeme
        self.write(tokentype + ' (' + lexeme + ')')
        self.write('\n')

    def visit_index_expr(self, index_expr):
        self.indent_write('IndexExpr:\n')
        self.indent += 1
        self.indent_write('INDEXED ID (')
        self.write(index_expr.identifier.lexeme)
        self.write(')\n')
        index_expr.expr.accept(self)
        self.indent -= 1

    def visit_list_expr(self, list_expr):
        self.indent_write('ListExpr:\n')
        self.indent += 1
        for expr in list_expr.expressions:
            expr.accept(self)
        self.indent -= 1

    def visit_read_expr(self, read_expr):
        self.indent_write('ReadExpr: ')
        if read_expr.is_read_int:
            self.write('READINT ')
        else:
            self.write('READSTR ')
        self.write('(')
        self.write(read_expr.msg.lexeme)
        self.write(')\n');

    def visit_complex_expr(self, complex_expr):
        self.indent_write('ComplexExpr:\n')
        self.indent += 1
        complex_expr.first_operand.accept(self)
        self.indent_write(complex_expr.math_rel.tokentype)
        self.write('\n')
        complex_expr.rest.accept(self)
        self.indent -= 1
