import ply.lex as lex
import ply.yacc as yacc
from model import *

keywords = {
    'if': 'IF',
    'else': 'ELSE',
    'and': 'AND',
    'or': 'OR',
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
             'COLON',
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
             'STRINGVAL',
             'ID',
             'CID',
             'EOL'
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
t_COLON = r'\;'
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
t_STRINGVAL = r'[\"].*[\"]'


def t_FLOATNUM(token):
    r'[0-9]+\.[0-9]+'
    return token


def t_INTNUM(token):
    r'[0-9]+'
    token.type = keywords.get(token.value, 'INTNUM')
    return token


def r_BOOLVAL(token):
    r'[true]|[false]'
    return token


def t_CID(token):
    r'[A-Z][a-zA-z0-9]*'
    token.type = keywords.get(token.value, 'CID')
    return token


def t_ID(token):
    r'[a-zA-Z][a-zA-z0-9]*'
    token.type = keywords.get(token.value, 'ID')
    return token


t_ignore = " \t"


def t_EOL(token):
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
    class : CLASS CID classparams class2 body
    '''
    p[0] = Class(name=p[2], body=p[5])
    print(p[0])


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
    bloque2 : RETURN bloque3
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
    p[0] = p[1]


def p_expresion(p):
    '''
    expresion : megaexp
    | ID PARIZQ expresion2 PARDER
   '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        print("TODO")


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
    if len(p) == 0:
        p[0] = None
    else:
        p[0] = RelationalOperand(p[1], p[2])


def p_superexp(p):
    '''
    superexp : exp oplog
    '''
    p[0] = RelationalOperation(p[1], p[2])


def p_megaexp(p):
    '''
    megaexp : superexp megaexpr
    '''
    p[0] = LogicalOperation(p[1], p[2])


def p_megaexpr(p):
    '''
    megaexpr : AND superexp megaexpr
    | OR superexp megaexpr
    | empty
    '''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = LogicalOperand(p[1], p[2], p[3])


def p_vars(p):
    '''
    vars : vars3 tipo vars2 COLON
    | vars3 tipo LIST vars2 COLON
    '''
    variables = []
    visibility = p[1]
    type = p[2]
    for var in p[3]:
        variables.append(VarDeclaration(var, type, visibility))
    p[0] = variables


def p_varsr(p):
    '''
    varsr : COMA ID varsr
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[2]] + p[3]


def p_vars2(p):
    '''
    vars2 : ID varsr
    '''
    p[0] = [p[1]] + p[2]


def p_vars3(p):
    '''
    vars3 : PRIVATE
    | empty
    '''
    p[0] = p[1]


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
    p[0] = [p[1]]


def p_asignacion(p):
    '''
    asignacion : ID asignacion3 IGUAL asignacion2 COLON
    '''
    p[0] = Assignment(p[1], p[4])


def p_asignacion2(p):
    '''
    asignacion2 : expresion
    | CORCHDER expresion asignacion2r CORCHIZQ
    | READ PARIZQ STRING PARDER
    '''
    if len(p) == 2:
        p[0] = p[1]


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
    condicionr : ELSE IF condicion2
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
    p[0] = p[1]


def p_factor(p):
    '''
    factor : PARIZQ expresion PARDER
    | factor2 varcte varcter
    '''
    if p[0] is None:
        p[0] = ConstantVar(p[2])
    else:
        p[0] = ArithmeticOperand(p[1], p[2])


def p_terminor(p):
    '''
    terminor : POR factor terminor
    | SOBRE factor terminor
    | empty
    '''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = TerminoR(p[1], p[2], p[3])


def p_termino(p):
    '''
    termino : factor terminor
    '''
    p[0] = Termino(p[1], p[2])


def p_exp(p):
    '''
    exp : termino expr
    '''
    p[0] = Exp(p[1], p[2])


def p_expr(p):
    '''
    expr : MAS termino expr
    | MENOS termino expr
    | empty
    '''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = ExpR(p[1], p[2], p[3])


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
    if p[1] is None:
        p[0] = p[1]
    else:
        p[0] = p[1]


def p_for(p):
    '''
    for : FOR PARIZQ ID IN for2 PARDER bloque
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
    | IN range FLECHITA bloque when2
    | ELSE FLECHITA bloque when2
    | empty
    '''


def p_fun(p):
    '''
    fun : vars3 FUN ID PARIZQ fun2 PARDER fun3 funbody
    '''
    body = p[8]
    body.vars += p[5]
    p[0] = Fun(name=p[3], type=p[7], visibility=p[1], body=body)


def p_fun2(p):
    '''
    fun2 : tipo ID funparamr
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [VarDeclaration(name=p[2], type=p[1], visibility=None)] + p[3]


def p_funparamr(p):
    '''
    funparamr : COMA tipo ID funparamr
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [VarDeclaration(name=p[3], type=p[2], visibility=None)] + p[4]


def p_fun3(p):
    '''
    fun3 : DOSPUNTOS tipo
    | empty
    '''
    if len(p) == 2:
        p[0] = "void"
    else:
        p[0] = p[2]


def p_funbody(p):
    '''
    funbody : LLAVEIZQ opc1 opc2 bloque2 LLAVEDER
    '''
    p[0] = FunBody(p[2], p[3])


def p_opc1(p):
    '''
    opc1 : vars multvarsdecl
    | empty
    '''
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1] + p[2]


def p_opc2(p):
    '''
    opc2 : estatuto
    | empty
    '''
    p[0] = p[1]


def p_body(p):
    '''
    body : LLAVEIZQ body2 funr MAIN PARIZQ PARDER bloque LLAVEDER
    '''
    p[0] = ClassBody(vars=p[2], funs=p[3])


def p_body2(p):
    '''
    body2 : vars multvarsdecl
    | empty
    '''
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1] + p[2]


def p_multvarsdecl(p):
    '''
    multvarsdecl : vars
    | empty
    '''
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1]


def p_funr(p):
    '''
    funr : fun funr
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]


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
parser = yacc.yacc(start='class')

'''
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    parser.parse(s)
    fun_directory.print()
'''

with open("test/test2.txt", 'r') as f:
    input = f.read()
    parser.parse(input)
