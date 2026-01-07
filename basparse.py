import ply.yacc as yacc
from basiclex import tokens

class Program:
    def __init__(self, statements):
        self.statements = statements

class Block:
    def __init__(self, statements):
        self.statements = statements

class Assign:
    def __init__(self, var, op, expr):
        self.var = var
        self.op = op
        self.expr = expr

class If:
    def __init__(self, cond, then_body, else_body=None):
        self.cond = cond
        self.then_body = then_body
        self.else_body = else_body

class While:
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class Echo:
    def __init__(self, expr):
        self.expr = expr

class Print:
    def __init__(self, expr):
        self.expr = expr

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Number:
    def __init__(self, value):
        self.value = value

class String:
    def __init__(self, value):
        self.value = value.strip('"').strip("'")

class Variable:
    def __init__(self, name):
        self.name = name



# GRAMMAR
precedence = (
    ('left', 'T_CONCAT'),
    ('left', 'T_PLUS', 'T_MINUS'),
    ('left', 'T_MULT', 'T_DIV', 'T_MOD'),
    ('nonassoc', 'T_IS_NOT_EQUAL', 'T_IS_GREATER_OR_EQUAL', 'T_IS_SMALLER_OR_EQUAL'),
)

def p_program(p):
    "program : T_OPEN_TAG stmt_list T_CLOSE_TAG"
    p[0] = Program(p[2])

def p_stmt_list(p):
    """stmt_list : stmt_list stmt
                 | stmt"""
    p[0] = p[1] + [p[2]] if len(p) == 3 else [p[1]]

def p_stmt(p):
    """stmt : assignment T_SEMICOLON
            | echo_stmt T_SEMICOLON
            | print_stmt T_SEMICOLON
            | if_stmt
            | while_stmt"""
    p[0] = p[1]

# -BLOCK
def p_block(p):
    "block : T_LBRACE stmt_list T_RBRACE"
    p[0] = Block(p[2])

# -ASSIGN
def p_assignment(p):
    """assignment : T_VARIABLE T_EQUAL expr
                  | T_VARIABLE T_PLUS_EQUAL expr
                  | T_VARIABLE T_MINUS_EQUAL expr
                  | T_VARIABLE T_MUL_EQUAL expr
                  | T_VARIABLE T_DIV_EQUAL expr
                  | T_VARIABLE T_MOD_EQUAL expr
                  | T_VARIABLE T_CONCAT_EQUAL expr"""
    p[0] = Assign(p[1], p[2], p[3])

# - IF 
def p_if_stmt(p):
    """if_stmt : T_IF T_LPAREN expr T_RPAREN block
               | T_IF T_LPAREN expr T_RPAREN block T_ELSE block"""
    if len(p) == 6:
        p[0] = If(p[3], p[5])
    else:
        p[0] = If(p[3], p[5], p[7])

# - WHILE 
def p_while_stmt(p):
    "while_stmt : T_WHILE T_LPAREN expr T_RPAREN block"
    p[0] = While(p[3], p[5])

# - IO 
def p_echo_stmt(p):
    "echo_stmt : T_ECHO expr"
    p[0] = Echo(p[2])

def p_print_stmt(p):
    "print_stmt : T_PRINT expr"
    p[0] = Print(p[2])

# - EXPRESSIONS 
def p_expr_binop(p):
    """expr : expr T_PLUS expr
            | expr T_MINUS expr
            | expr T_MULT expr
            | expr T_DIV expr
            | expr T_MOD expr
            | expr T_CONCAT expr
            | expr T_IS_NOT_EQUAL expr
            | expr T_IS_GREATER_OR_EQUAL expr
            | expr T_IS_SMALLER_OR_EQUAL expr"""
    p[0] = BinOp(p[1], p[2], p[3])

def p_expr_group(p):
    "expr : T_LPAREN expr T_RPAREN"
    p[0] = p[2]

def p_expr_number(p):
    """expr : T_LNUMBER
            | T_DNUMBER"""
    p[0] = Number(p[1])

def p_expr_string(p):
    "expr : T_CONSTANT_ENCAPSED_STRING"
    p[0] = String(p[1])

def p_expr_variable(p):
    "expr : T_VARIABLE"
    p[0] = Variable(p[1])

def p_error(p):
    if p:
        print(f"Syntax error di token {p.type}, value={p.value}")
    else:
        print("Syntax error di EOF")

parser = yacc.yacc()
