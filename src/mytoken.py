PRINT = 'PRINT'
PRINTLN = 'PRINTLN'
READINT = 'READINT'
READSTR = 'READSTR'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
SEMICOLON = 'SEMICOLON'
ID = 'ID'
LBRACKET = 'LBRACKET'
RBRACKET = 'RBRACKET'
STRING = 'STRING'
INT = 'INT'
BOOL = 'BOOL'
COMMA = 'COMMA'
ASSIGN = 'ASSIGN'
PLUS = 'PLUS'
MINUS = 'MINUS'
DIVIDE = 'DIVIDE'
MULTIPLY = 'MULTIPLY'
MODULUS = 'MODULUS'
IF = 'IF'
THEN = 'THEN'
ELSEIF = 'ELSEIF'
ELSE = 'ELSE'
END = 'END'
NOT = 'NOT'
AND = 'AND'
OR = 'OR'
EQUAL = 'EQUAL'
LESS_THAN = 'LESS_THAN'
GREATER_THAN = 'GREATER_THAN'
LESS_THAN_EQUAL = 'LESS_THAN_EQUAL'
GREATER_THAN_EQUAL = 'GREATER_THAN_EQUAL'
NOT_EQUAL = 'NOT_EQUAL'
WHILE = 'WHILE'
DO = 'DO'
EOS = 'EOS'


class Token(object):
    """
    creates a token class that has a token type (see above), lexeme, line number,
    and column number.
    """
    def __init__(self, tokentype, lexeme, line, column):
        self.tokentype = tokentype
        self.lexeme = lexeme
        self.line = line
        self.column = column

    def __str__(self):
        return "%s '%s' %s:%s" % (self.tokentype, self.lexeme, self.line, self.column)
