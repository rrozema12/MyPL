import mytoken
import error


class Lexer(object):
    """
    Creates a lexer that has an input stream, which is a program or a .txt file.
    """

    def __init__(self, input_stream):
        self.line = 1
        self.column = 0
        self.input_stream = input_stream

    def __peek(self):
        """ Gets the next character in the input stream without advancing to the next position """
        pos = self.input_stream.tell()
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol

    def __read(self):
        """ returns the next character and advances a postition in the input stream"""
        return self.input_stream.read(1)

    def advance_column(self):
        """ increments column value by 1"""
        self.column += 1

    def advance_line(self):
        """increments line number by 1 and resents column value to 0 """
        self.column = 0
        self.line += 1

    def next_token(self):
        """
        Gets what is at the current position in the parse and assigns it a token.
        """
        symbol = self.__read()
        self.advance_column()

        """ Checks to see if it the parser is at the end of the file """
        if symbol == '':
            return mytoken.Token(mytoken.EOS, "", self.line, self.column)

        """ Checks for ta newline character in the file """
        if symbol == '\n':
            self.advance_line()
            return self.next_token()

        """ checks for a comment so the parser can skip that part of the code """
        if symbol == '#':
            go = True
            while go:
                if self.__peek() == '\n':
                    self.__read()
                    self.advance_line()
                    go = False
                else:
                    self.__read()
                    self.advance_column()
            return self.next_token()

        if symbol.isspace():
            return self.next_token()

        """ If the lexeme is an int it returns the value """
        if symbol.isdigit():
            column_at_start = self.column
            line_at_start = self.line
            cur_num = symbol
            while self.__peek().isdigit():
                cur_num += self.__read()
                self.advance_column()
            return mytoken.Token(mytoken.INT, cur_num, line_at_start, column_at_start)

        """checks to see if the lexeme is a aplhabetical and returns the value"""
        if symbol.isalpha():
            column_at_start = self.column
            line_at_start = self.line
            cur_string = symbol
            while self.__peek().isalpha() or self.__peek().isdigit() or self.__peek() == '_':
                cur_string += self.__read()
                self.advance_column()

            if cur_string == 'println':
                return mytoken.Token(mytoken.PRINTLN, cur_string, line_at_start, column_at_start)
            if cur_string == 'print':
                return mytoken.Token(mytoken.PRINT, cur_string, line_at_start, column_at_start)
            if cur_string == 'while':
                return mytoken.Token(mytoken.WHILE, cur_string, line_at_start, column_at_start)
            if cur_string == 'if':
                return mytoken.Token(mytoken.IF, cur_string, line_at_start, column_at_start)
            if cur_string == 'end':
                return mytoken.Token(mytoken.END, cur_string, line_at_start, column_at_start)
            if cur_string == 'else':
                return mytoken.Token(mytoken.ELSE, cur_string, line_at_start, column_at_start)
            if cur_string == 'elseif':
                return mytoken.Token(mytoken.ELSEIF, cur_string, line_at_start, column_at_start)
            if cur_string == 'do':
                return mytoken.Token(mytoken.DO, cur_string, line_at_start, column_at_start)
            if cur_string == 'then':
                return mytoken.Token(mytoken.THEN, cur_string, line_at_start, column_at_start)
            if cur_string == 'readint':
                return mytoken.Token(mytoken.READINT, cur_string, line_at_start, column_at_start)
            if cur_string == 'readstr':
                return mytoken.Token(mytoken.READSTR, cur_string, line_at_start, column_at_start)
            if cur_string == 'and':
                return mytoken.Token(mytoken.AND, cur_string, line_at_start, column_at_start)
            if cur_string == 'or':
                return mytoken.Token(mytoken.OR, cur_string, line_at_start, column_at_start)
            if cur_string == 'not':
                return mytoken.Token(mytoken.NOT, cur_string, line_at_start, column_at_start)
            if cur_string == 'true' or cur_string == 'false':
                return mytoken.Token(mytoken.BOOL, cur_string, line_at_start, column_at_start)
            else:
                return mytoken.Token(mytoken.ID, cur_string, line_at_start, column_at_start)

        """Checks to see if symbol is a quotation"""
        if symbol == '"':
            column_at_start = self.column
            line_at_start = self.line
            go = True
            cur_string = ''
            while go:
                if self.__peek() == '\n':
                    raise error.Error("reached newline reading string", self.line, self.column)
                if self.__peek() == '"':
                    self.__read()
                    self.advance_column()
                    go = False
                else:
                    cur_string += self.__read()
                    self.advance_column()
            return mytoken.Token(mytoken.STRING, cur_string, line_at_start, column_at_start)

        if symbol == '=':
            if self.__peek() == '=':
                self.__read()
                self.advance_column()
                return mytoken.Token(mytoken.EQUAL, '==', self.line, self.column)
            else:
                return mytoken.Token(mytoken.ASSIGN, '=', self.line, self.column)

        if symbol == '<':
            if self.__peek() == '=':
                self.__read()
                self.advance_column()
                return mytoken.Token(mytoken.LESS_THAN_EQUAL, '<=', self.line, self.column)

            else:
                return mytoken.Token(mytoken.LESS_THAN, '<', self.line, self.column)

        if symbol == '>':
            if self.__peek() == '=':
                self.__read()
                self.advance_column()
                return mytoken.Token(mytoken.GREATER_THAN_EQUAL, '>=', self.line, self.column)

            else:
                return mytoken.Token(mytoken.GREATER_THAN, '>', self.line, self.column)

        if symbol == '!':
            if self.__peek() == '=':
                self.__read()
                self.advance_column()
                return mytoken.Token(mytoken.NOT_EQUAL, '!=', self.line, self.column)

        if symbol == ',':
            return mytoken.Token(mytoken.COMMA, ',', self.line, self.column)

        if symbol == ';':
            cur_line = self.line
            cur_column = self.column
            return mytoken.Token(mytoken.SEMICOLON, ';', cur_line, cur_column)

        """Mathematical Lexemes"""
        if symbol == '+':
            return mytoken.Token(mytoken.PLUS, '+', self.line, self.column)

        if symbol == '-':
            return mytoken.Token(mytoken.MINUS, '-', self.line, self.column)

        if symbol == '*':
            return mytoken.Token(mytoken.MULTIPLY, '*', self.line, self.column)

        if symbol == '/':
            return mytoken.Token(mytoken.DIVIDE, '/', self.line, self.column)

        if symbol == '%':
            return mytoken.Token(mytoken.MODULUS, '%', self.line, self.column)

        """Brackets and Parenthesis"""
        if symbol == '[':
            return mytoken.Token(mytoken.LBRACKET, '[', self.line, self.column)

        if symbol == ']':
            return mytoken.Token(mytoken.RBRACKET, ']', self.line, self.column)

        if symbol == '(':
            return mytoken.Token(mytoken.LPAREN, '(', self.line, self.column)

        if symbol == ')':
            return mytoken.Token(mytoken.RPAREN, ')', self.line, self.column)

        else:

            """
            Throws an error just in case the file could not be parsed.
            """
            raise error.Error("'%s' could not be parsed" % symbol, self.line, self.column)
