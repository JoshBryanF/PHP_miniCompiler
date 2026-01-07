import ply.lex as lex

# --- Daftar token ---
tokens = (
    # Tag PHP
    'T_OPEN_TAG',
    'T_CLOSE_TAG',

    # Identifiers & variabel
    'T_VARIABLE',
    'T_STRING',
    'T_LNUMBER',
    'T_DNUMBER',
    'T_CONSTANT_ENCAPSED_STRING',

    # Operator aritmatika
    'T_PLUS',
    'T_MINUS',
    'T_MULT',
    'T_DIV',
    'T_MOD',
    'T_CONCAT',

    # Operator gabungan
    'T_EQUAL',
    'T_PLUS_EQUAL',
    'T_MINUS_EQUAL',
    'T_MUL_EQUAL',
    'T_DIV_EQUAL',
    'T_MOD_EQUAL',
    'T_CONCAT_EQUAL',

    # Operator perbandingan
    'T_IS_NOT_EQUAL',
    'T_IS_GREATER_OR_EQUAL',
    'T_IS_SMALLER_OR_EQUAL',

    # Simbol
    'T_SEMICOLON',
    'T_LPAREN',
    'T_RPAREN',
    'T_LBRACE',
    'T_RBRACE',

    # Komentar
    'T_COMMENT',
    'T_DOC_COMMENT',

    # Keyword
    'T_IF',
    'T_ELSE',
    'T_WHILE',
    'T_FOR',
    'T_PRINT',
    'T_ECHO',
)

# --- Pola regex sederhana ---
t_T_OPEN_TAG   = r'<\?php'
t_T_CLOSE_TAG  = r'\?>'
t_T_PLUS       = r'\+'
t_T_MINUS      = r'-'
t_T_MULT       = r'\*'
t_T_DIV        = r'/'
t_T_MOD        = r'%'
t_T_CONCAT     = r'\.'
t_T_EQUAL      = r'='
t_T_SEMICOLON  = r';'
t_T_LPAREN     = r'\('
t_T_RPAREN     = r'\)'
t_T_LBRACE     = r'\{'
t_T_RBRACE     = r'\}'

# --- Operator gabungan ---
t_T_PLUS_EQUAL     = r'\+='
t_T_MINUS_EQUAL    = r'-='
t_T_MUL_EQUAL      = r'\*='
t_T_DIV_EQUAL      = r'/='
t_T_MOD_EQUAL      = r'%='
t_T_CONCAT_EQUAL   = r'\.='

# --- Operator perbandingan ---
t_T_IS_NOT_EQUAL          = r'(!=|<>)'
t_T_IS_GREATER_OR_EQUAL   = r'(>=|>)'
t_T_IS_SMALLER_OR_EQUAL   = r'(<=|<)'


# --- Token kompleks ---
def t_T_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_T_LNUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_T_DNUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_T_CONSTANT_ENCAPSED_STRING(t):
    r'(\"([^\\"]|\\.)*\")|(\'([^\\\']|\\.)*\')'
    return t

# --- Keyword / Identifier ---
def t_T_STRING(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {
        'if': 'T_IF',
        'else': 'T_ELSE',
        'while': 'T_WHILE',
        'for': 'T_FOR',
        'print': 'T_PRINT',
        'echo': 'T_ECHO',
    }
    t.type = keywords.get(t.value.lower(), 'T_STRING')
    return t

# --- Komentar ---
def t_T_COMMENT(t):
    r'(//[^\n]*|\#[^\n]*)'
    pass

def t_T_DOC_COMMENT(t):
    r'/\*\*([^*]|\*+[^*/])*\*+/'
    pass

# --- Abaikan spasi dan newline ---
t_ignore = ' \t\r\n'

# --- Error handling ---
def t_error(t):
    print(f"Karakter ilegal: '{t.value[0]}' pada posisi {t.lexpos}")
    t.lexer.skip(1)

# --- Buat lexer ---
lexer = lex.lex()