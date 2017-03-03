# Interpreter for a Made up Language MyPL

## Informal Description of MyPL Language
The language supports basic assignment statements, arithmetic expressions, conditionals, loops, lists, and basic input/output. All variables are implicitly typed (i.e., the types of variables are inferred from their values). Programs consist of a sequence of statements given within a single file.  

The language constructs supported by MyPL are described in more detail below.

1. **Primitive Data Types**   
    > integer, string (using double quotes ""), and boolean (true and false)   

2. **List Types**   
    > MyPL uses Python-like lists.

3. **Assignment Statements**   
    > An assignment statement takes the form “var = expr;” where var is a valid identifier (a letter followed by zero or more letters, digits, or underscores) and expr is a valid expression. Assignment statements bind the variable to the value that results from evaluating the expression. Assignment statements must end in a semicolon.

4. **Output Statements**   
    > “print(expr);” or “println(expr);”

5. **Math Operators**
    > +, -, \*, /, and %

6. **Relational Operators**
    > ==, <, >, <=, >=, and !=

7. **Boolean Connectives**
    > and, or, and not

8. **Input Expressions**
    > readint(msg) and readstr(msg) where msg is of type string.

9. **While Statements**
    > A while statement takes the form “while bool-expr do stmts end”, where bool-expr is a Boolean expression and stmts is a list of statements.

10. **Conditional Statements**
    > A condition statement takes the form “if bool-expr then stmts elseif bool-expr then stmts else stmts end”. A conditional statement can have zero or more elseif clauses and zero or one else clause. A conditional statement always ends with an “end” reserved word. Note that elseif is a distinct reserved word and should be used instead of an else followed by an if.

11. **Comments**
    > MyPL uses Python-like comments (#)

## Grammar Rules
The proper syntax is defined by these grammars:
```
<stmts> ::= <stmt> <stmts> | empty
<stmt> ::= <output> | <assign> | <cond> | <loop>
<output> ::= PRINT LPAREN <expr> RPAREN SEMICOLON | PRINTLN LPAREN <expr> RPAREN SEMICOLON
<input> ::= READINT LPAREN STRING RPAREN | READSTR LPAREN STRING RPAREN
<assign> ::= ID <listindex> ASSIGN <expr> SEMICOLON
<listindex> ::= LBRACKET <expr> RBRACKET | empty
<expr> ::= <value> <exprt>
<exprt> ::= <math_rel> <expr> | empty
<value> ::= ID <listindex> | STRING | INT | BOOL | <input> | LBRACKET <exprlist> RBRACKET
<exprlist> ::= <expr> <exprtail> | empty
<exprtail> ::= COMMA <expr> <exprtail> | empty
<math_rel> ::= PLUS | MINUS | DIVIDE | MULTIPLY | MODULUS
<cond> ::= IF <bexpr> THEN <stmts> <condt> END
<condt> ::= ELSEIF <bexpr> THEN <stmts> <condt> | ELSE <stmts> | empty
<bexpr> ::= <expr> <bexprt> | NOT <expr> <bexprt>
<bexprt> ::= <bool_rel> <expr> <bconnct> | empty
<bconnct> ::= AND <bexpr> | OR <bexpr> | empty
<bool_rel> ::= EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_EQUAL | GREATER_THAN_EQUAL | NOT_EQUAL
<loop> ::= WHILE <bexpr> DO <stmts> END
```
## Sample MyPL Programs
The following are some examples of programs in MyPL:
```
# obligatory hello world program
println("Hello world!");


# simple conditional statement
x = readint("Enter an int: ");
y = readint("Enter an int: ");
if x > y then
    println("The first int was bigger than the second!");
elseif y > x then
    println("The second int was bigger than the first!");
else
    println("You entered the same value twice!");
end


# simple while statement
z = readint("Enter an int: ");
i = 0;
while z > 2 do
    z = z / 2;
    i = i + 1;
end
print("z = ");
print(z);
print(", i = ");
println(i);
```

## Running the application
Run the application with this command
```bash
python hw6.py my_pl_file.txt
```

## Example Output
TODO
