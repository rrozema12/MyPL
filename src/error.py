class Error(Exception):
    """Initializes an error with a message, line number, and column number.
    Also overrides the string method to print out the error."""

    def __init__(self, message, line, column):
        self.message = message
        self.line = line
        self.column = column

    def __str__(self):
        s = ''
        s += 'error: ' + self.message
        s += ' at line ' + str(self.line)
        s += ' column ' + str(self.column)
        return s
