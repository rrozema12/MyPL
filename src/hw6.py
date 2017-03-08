"""
Ryan Rozema
hw6.py
hw6
"""

import sys
import lexer
import parser
import error
import mypl_type_checker as type_checker
import mypl_interpreter


def main(filename):
    try:
        file_stream = open(filename, 'r')
        the_lexer = lexer.Lexer(file_stream)
        the_parser = parser.Parser(the_lexer)
        stmt_list = the_parser.parse()
        checker = type_checker.TypeChecker()
        stmt_list.accept(checker)
        interpreter = mypl_interpreter.Interpreter()
        stmt_list.accept(interpreter)

    except IOError as e:
        print "error: unable to open file '" + filename + "'"
        sys.exit(1)
    except error.Error as e:
        print e
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage:', sys.argv[0], 'source - code - file'
        sys.exit(1)
    else:
        main(sys.argv[1])
