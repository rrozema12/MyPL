"""
Ryan Rozema
mypl_type_checker.py
hw5
"""
from mypl_ast import Visitor
from mypl_symbol_table import *
import mytoken as token
from error import Error


class TypeChecker(Visitor):
    def __init__(self):
        """ Default Constructor """
        self.sym_table = SymbolTable()
        self.current_type = None

    def visit_stmt_list(self, stmt_list):
        """ A function that will visit the statement list when required """
        self.sym_table.push_environment()
        for stmt in stmt_list.stmts:
            stmt.accept(self)
        self.sym_table.pop_environment()

    def visit_simple_bool_expr(self, simple_bool_expr):
        """ A function that will visit a simple boolean expression. This function
            just accepts a simple boolean expression """
        simple_bool_expr.expr.accept(self)

    def visit_complex_bool_expr(self, complex_bool_expr):
        """ This function deals with a complex boolean expresson by taking the
            second half of the expresson and converting it to the current token,
            then comparing that to the first token and making sure that they are
            of the same type."""
        middle_node = complex_bool_expr.second_expr.term
        if complex_bool_expr.has_bool_connector:
            complex_bool_expr.rest.accept(self) # rest is stored to curr token
            if self.sym_table.variable_exists(middle_node.lexeme):
                type = self.sym_table.get_variable_type(middle_node.lexeme)
                if self.current_type != type:
                    msg = "expecting " + type + " but got " + self.current_type
                    raise Error(msg, middle_node.line, middle_node.column)
            else:
                msg = middle_node.lexeme + " is used before it was defined"
                raise Error(msg, middle_node.line, middle_node.column)
        complex_bool_expr.second_expr.accept(self) # second expr stored as curr token
        first_node = complex_bool_expr.first_expr.term
        if self.sym_table.variable_exists(first_node.lexeme):
            type = self.sym_table.get_variable_type(first_node.lexeme)
            if self.current_type != type:
                msg = "expecting " + type + " but got " + self.current_type
                raise Error(msg, first_node.line, first_node.column)
        else:
            msg = first_node.lexeme + " is used before it is defined"
            raise Error(msg, first_node.line, first_node.column)

    def visit_if_stmt(self, if_stmt):
        """ This function handles the if statements. """
        if_stmt.if_part.bool_expr.accept(self)
        self.sym_table.push_environment()
        if_stmt.if_part.stmt_list.accept(self)
        self.sym_table.pop_environment()
        for elseif in if_stmt.elseifs:
            elseif.bool_expr.accept(self)
            self.sym_table.push_environment()
            elseif.stmt_list.accept(self)
            self.sym_table.pop_environment()
        if if_stmt.has_else:
            self.sym_table.push_environment()
            if_stmt.else_stmts.accept(self)
            self.sym_table.pop_environment()

    def visit_while_stmt(self, while_stmt):
        """ This function handles the while statements. """
        while_stmt.bool_expr.accept(self)
        self.sym_table.push_environment()
        while_stmt.stmt_list.accept(self)
        self.sym_table.pop_environment()

    def visit_print_stmt(self, print_stmt):
        """ This function handles the print statements. """
        print_stmt.expr.accept(self)

    def visit_assign_stmt(self, assign_stmt):
        """ This function deals with assignment statement by taking the
            getting each half of the assignment statement and comparing the
            two types to make sure that they are the same."""
        lhs = assign_stmt.lhs
        assign_stmt.rhs.accept(self)
        if lhs.tokentype == token.ID:
            lhs_lexeme = lhs.lexeme
            if self.sym_table.variable_exists(lhs_lexeme):
                lhs_type = self.sym_table.get_variable_type(lhs_lexeme)
                if self.current_type != lhs_type:
                    msg = "expecting " + lhs_type + " but got " + self.current_type
                    raise Error(msg, lhs.line, lhs.column)
            else:
                self.sym_table.add_variable(lhs_lexeme)
                self.sym_table.set_variable_type(lhs_lexeme, self.current_type)

    def visit_simple_expr(self, simple_expr):
        """ This function deals with a simple expression. """
        term = simple_expr.term
        if term.tokentype == token.ID:
            if self.sym_table.variable_exists(term.lexeme):
                self.current_type = self.sym_table.get_variable_type(term.lexeme)
            else:
                msg = term.lexeme + " is used before it is defined"
                raise Error(msg, term.line, term.column)
        else:
            self.current_type = term.tokentype

    def visit_index_expr(self, index_expr):
        """Will implement in the next assignment for extra credit"""
        print "Visit Index Expr"

    def visit_list_expr(self, list_expr):
        """Will implement in the next assignment for extra credit"""
        print "Visit List Expr"

    def visit_read_expr(self, read_expr):
        """This function handles the read expressions"""
        node = read_expr.msg
        if read_expr.is_read_int:
            if node.tokentype != token.STRING:
                msg = "expecting INT but got " + node.tokentype
                raise Error(msg, node.line, node.column)
            self.current_type = token.INT
        else:
            if node.tokentype != token.STRING:
                msg = "expecting STRING but got " + node.tokentype
                raise Error(msg, node.line, node.column)
            self.current_type = token.STRING

    def visit_complex_expr(self, complex_expr):
        """This function handles the complex expressions"""
        complex_expr.rest.accept(self)
        rhs = self.current_type
        complex_expr.first_operand.accept(self)
        first_op = complex_expr.first_operand.term
        if self.current_type != rhs:
            msg = "expecting " + rhs + " but got " + self.current_type
            raise Error(msg, first_op.line, first_op.column)
