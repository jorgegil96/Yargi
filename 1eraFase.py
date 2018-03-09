import ply.lex as lex
import ply.yacc as yacc

keywords = {
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'string': 'STRING',
    'fun': 'FUN',
    'when': 'WHEN',
    'for': 'FOR',
    'while': 'WHILE',
    'in': 'IN',
    'return': 'RETURN',
    'write': 'WRITE',
    'read': 'READ',
    'and': 'AND',
    'or': 'OR',
    'global': 'GLOBAL',
    'class': 'CLASS',
    'list': 'LIST',
    'range': 'RANGE',
    'main': 'MAIN',
    'private': 'PRIVATE'
}

tokens = [
             'INTNUM',
             'FLOATNUM',
             'BOOLVAL',
             'PARIZQ',
             'PARDER',
             'LLAVEIZQ',
             'LLAVEDER',
             'MAS',
             'MENOS',
             'POR',
             'SOBRE',
             'DOSPUNTOS',
             'COMA',
             'MAYORQUE',
             'MENORQUE',
             'DIFERENTE',
             'IGUALIGUAL',
             'MENOROIGUAL',
             'MAYOROIGUAL',
             'COMENTARIOS',
             'CORCHIZQ',
             'CORCHDER',
             'COMILLAS',
             'PUNTO',
             'IGUAL',
             'PUNTOSRANGO',
             'FLECHITA',
             'STRING',
             'ID',
             'CID',
             'EOL',
             'WS',
         ] + list(keywords.values())

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_SOBRE = r'\/'
t_DOSPUNTOS = r'\:'
t_COMA = r'\,'
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_DIFERENTE = r'\!='
t_IGUALIGUAL = r'\=='
t_MENOROIGUAL = r'\<='
t_MAYOROIGUAL = r'\>='
t_COMENTARIOS = r'\//'
t_CORCHIZQ = r'\['
t_CORCHDER = r'\]'
t_COMILLAS = r'\"'
t_PUNTO = r'\.'
t_IGUAL = r'='
t_PUNTOSRANGO = r'\.\.'
t_FLECHITA = r'\-\>'
t_STRING = r'[\"].*[\"]'
t_EOL = r'\n'
t_WS = r'\s'



def t_FLOATNUM(token):
    r'[0-9]+\.[0-9]+'
    return token


def t_INTNUM(token):
    r'[0-9]+'
    return token


def r_BOOLVAL(token):
    r'[true]|[false]'
    return token


def t_ID(token):
    r'[a-zA-Z][a-zA-z0-9]*'
    token.type = keywords.get(token.value, 'ID')
    return token


def t_CID(token):
    r'[A-Z][a-zA-z0-9]*'
    token.type = keywords.get(token.value, 'CID')


t_ignore = "\t"


def t_newline(token):
    r'\n+'
    token.lexer.lineno += token.value.count("\n")


'''
def t_error (token):
    print("Error")
    token.lexer.skip(1)
'''


def p_resultado(p):
    '''
    resultado : class
    '''


def p_class(p):
    '''
    class : CLASS WS ID classparams class2 body
    '''


def p_class2(p):
    '''
    class2 : DOSPUNTOS ID PARIZQ vars2 PARDER
    | empty
    '''


def p_classparams(p):
    '''
    classparams : PARIZQ classparams2 PARDER
    '''


def p_classparams2(p):
    '''
    classparams2 : vars
    | empty
    '''


def p_bloque(p):
    '''
    bloque : LLAVEIZQ estatuto bloque2 LLAVEDER
    '''


def p_bloque2(p):
    '''
    bloque2 : RETURN WS bloque3
    | empty
    '''


def p_bloque3(p):
    '''
    bloque3 : expresion
    | empty
    '''

def p_varcte(p):
    '''
    varcte : ID
    | INTNUM
    | FLOATNUM
    | BOOLVAL
    | STRING
    | ID CORCHIZQ varcte CORCHDER
    | ID PUNTO ID
    | ID PARIZQ expresion2 PARDER
    '''


def p_expresion(p):
    '''
    expresion : exp oplog
    | ID PARIZQ expresion2 PARDER
   '''

def p_expresionr(p):
    '''
    expresionr : COMA expresion expresionr
    | empty
    '''

def p_expresion2(p):
    '''
    expresion2 : expresion expresionr
    | empty
    '''

def p_oplog(p):
    '''
    oplog : MAYORQUE exp
    | MENORQUE exp
    | DIFERENTE exp
    | MAYOROIGUAL exp
    | MENOROIGUAL exp
    | IGUALIGUAL exp
    | empty
    '''

def p_vars(p):
    '''
    vars : vars3 WS tipo WS vars2
    | vars3 WS tipo WS LIST WS vars2
    '''


def p_varsr(p):
    '''
    varsr : COMA ID varsr
    | empty
    '''


def p_vars2(p):
    '''
    vars2 : ID varsr
    | empty
    '''

def p_vars3(p):
    '''
    vars3 : PRIVATE
    | empty
    '''


def p_estatuto(p):
    '''
    estatuto : asignacion estatuto
    | condicion estatuto
    | escritura estatuto
    | for estatuto
    | while estatuto
    | when estatuto
    | llamada estatuto
    | empty
    '''


def p_asignacion(p):
    '''
    asignacion : ID asignacion3 IGUAL asignacion2
    '''


def p_asignacion2(p):
    '''
    asignacion2 : expresion
    | CORCHDER expresion asignacion2r CORCHIZQ
    | READ PARIZQ STRING PARDER
    '''


def p_asignacion2r(p):
    '''
    asignacion2r : COMA expresion asignacion2r
    | empty
    '''


def p_asignacion3(p):
    '''
    asignacion3 : CORCHIZQ expresion CORCHDER
    | PUNTO ID
    | empty
    '''


def p_condicion(p):
    '''
    condicion : IF condicion2 condicionr estatutor
    '''


def p_condicion2(p):
    '''
    condicion2 : PARIZQ expresion PARDER bloque
    '''


def p_condicionr(p):
    '''
    condicionr : ELSE WS IF condicion2
    | empty
    '''


def p_estatutor(p):
    '''
    estatutor : ELSE bloque
    | empty
    '''


def p_escritura(p):
    '''
    escritura : WRITE PARIZQ esc1 esc2 PARDER
    '''


def p_esc1(p):
    '''
    esc1 : expresion
    | STRING
    '''


def p_esc2(p):
    '''
    esc2 : COMA esc1 esc2
    | empty
    '''

def p_tipo(p):
    '''
    tipo : INT
    | FLOAT
    | BOOL
    | STRING
    | CID
    '''

def p_factor(p):
    '''
    factor : PARIZQ expresion PARDER
    | factor2 varcte varcter
    '''

def p_terminor(p):
    '''
    terminor : POR factor terminor
    | SOBRE factor terminor
    | empty
    '''

def p_termino(p):
    '''
    termino : factor terminor
    '''

def p_exp(p):
    '''
    exp : termino expr
    '''


def p_expr(p):
    '''
    expr : MAS termino expr
    | MENOS termino expr
    | empty
    '''


def p_varcter(p):
    '''
    varcter : COMA varcte varcter
    | empty
    '''


def p_factor2(p):
    '''
    factor2 : MAS
    | MENOS
    | empty
    '''

def p_for(p):
    '''
    for : FOR PARIZQ ID WS IN WS for2 PARDER bloque
    '''


def p_for2(p):
    '''
    for2 : ID
    | range
    '''


def p_range(p):
    '''
    range : INTNUM PUNTOSRANGO INTNUM
    '''


def p_while(p):
    '''
    while : WHILE PARIZQ expresion PARDER bloque
    '''


def p_when(p):
    '''
    when : WHEN PARIZQ expresion PARDER LLAVEIZQ when2 LLAVEDER
    '''


def p_when2(p):
    '''
    when2 : varcte varcter FLECHITA bloque when2
    | IN WS range FLECHITA bloque when2
    | ELSE FLECHITA bloque when2
    | empty
    '''


def p_fun(p):
    '''
    fun : vars3 WS FUN WS ID PARIZQ fun2 PARDER fun3 funbody
    '''


def p_fun2(p):
    '''
    fun2 : tipo WS ID WS fun2
    | empty
    '''


def p_fun3(p):
    '''
    fun3 : DOSPUNTOS tipo
    | empty
    '''


def p_funbody(p):
    '''
    funbody : LLAVEIZQ opc1 WS opc2 WS bloque2 LLAVEDER
    '''

def p_opc1(p):
    '''
    opc1 : vars
    | empty
    '''

def p_opc2(p):
    '''
    opc2 : estatuto
    | empty
    '''

def p_body(p):
    '''
    body : LLAVEIZQ body2 WS funr WS MAIN PARIZQ PARDER bloque LLAVEDER
    '''


def p_body2(p):
    '''
    body2 : vars
    | empty
    '''


def p_funr(p):
    '''
    funr : fun WS funr
    | empty
    '''

def p_llamada(p):
    '''
    llamada : ID PARIZQ expresion expresionr PARDER
    | empty
    '''


def p_error(p):
    print("Syntax error at '%s'" % p.value)


def p_empty(p):
    '''empty : '''


lex.lex()
parser = yacc.yacc(start='body')


while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    parser.parse(s)
