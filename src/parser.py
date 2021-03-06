import ply.lex as lex
import ply.yacc as yacc

from src.semantics.model import *

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
    'data': 'DATA',
    'class': 'CLASS',
    'interface': 'INTERFACE',
    'list': 'LIST',
    'range': 'RANGE',
    'main': 'MAIN',
    'private': 'PRIVATE'
}

tokens = [
             'INTNUM',
             'FLOATNUM',
             'TRUE',
             'FALSE',
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
             'NULL',
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


def t_FLOATNUM(token):
    r'[0-9]+\.[0-9]+'
    token.type = keywords.get(token.value, 'FLOATNUM')
    token.value = float(token.value)
    return token


def t_INTNUM(token):
    r'[0-9]+'
    token.type = keywords.get(token.value, 'INTNUM')
    token.value = int(token.value)
    return token


def t_TRUE(token):
    'true'
    token.type = keywords.get(token.value, 'TRUE')
    token.value = True
    return token


def t_FALSE(token):
    'false'
    token.type = keywords.get(token.value, 'FALSE')
    token.value = False
    return token


def t_NULL(token):
    'null'
    token.type = keywords.get(token.value, 'NULL')
    token.value = None
    return token


def t_CID(token):
    r'[A-Z][a-zA-z0-9]*'
    token.type = keywords.get(token.value, 'CID')
    return token


def t_ID(token):
    r'[a-zA-Z][a-zA-z0-9]*'
    token.type = keywords.get(token.value, 'ID')
    return token


def t_STRINGVAL(token):
    r'[\"][^"]*[\"]'
    token.type = keywords.get(token.value, 'STRINGVAL')
    token.value = str(token.value)[1:-1]
    return token


t_ignore = " \t"


def t_EOL(token):
    r'\n+'
    token.lexer.lineno += token.value.count("\n")


'''
Parses a series of interfaces (0 or more), followed by a series of classes (1 or more).
Returns a Pair containing a list of interfaces and a list of classes.
'''
def p_file(p):
    '''
    file : interface_r class classr
    '''
    p[0] = p[1], [p[2]] + p[3]


'''
Parses a series of interfaces.
An interface is defined with the following syntax:
    interface MyInterface {
        fun foo();
        fun bar(int x=;
    }
Returns a list containing the available interfaces or an empty list if none were declared.
'''
def p_interface_r(p):
    '''
    interface_r : INTERFACE CID interface_body interface_r
        | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [Interface(p[2], p[3])] + p[4]


def p_interface_body(p):
    '''
    interface_body : LLAVEIZQ interface_fun interface_fun_r LLAVEDER
    '''
    p[0] = [p[2]] + p[3]


def p_interface_fun(p):
    '''
    interface_fun : FUN ID PARIZQ fun2 PARDER COLON
    '''
    p[0] = InterfaceFun(p[2], p[4])


def p_interface_fun_r(p):
    '''
    interface_fun_r : interface_fun interface_fun_r
        | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]


def p_classr(p):
    '''
    classr : class classr
        | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]


'''
Parses a class or a data class.
A class follows the syntax:
    class MyClass() : MyInterface, MySuperClass() {
        < functions >
        < main >
    }
A data classes follows the syntax:
    data class MyDataClass(int x, bool y)
    
Returns a Class object containing the information of the declared class.
'''
def p_class(p):
    '''
    class : CLASS CID classparams class2 body
        | DATA CLASS CID classparams
    '''
    if len(p) == 6:
        interfaces, parent = p[4]
        p[0] = Class(name=p[2], members=p[3], body=p[5], class_parent=parent, interfaces=interfaces)
    else:
        p[0] = Class(name=p[3], members=p[4], body=None, class_parent=None, interfaces=[])


def p_class2(p):
    '''
    class2 : DOSPUNTOS class_extras
        | empty
    '''
    if len(p) == 2:
        p[0] = [], None
    elif len(p) == 3:
        p[0] = p[2]


def p_class_extras(p):
    '''
    class_extras : CID class_extras_2
    '''
    arg1, arg2, arg3, type = p[2]
    if type == "SUPERCLASS":
        p[0] = [], ClassParent(p[1], arg2)
    elif type == "BOTH":
        p[0] = [p[1]] + arg2, arg3
    else:
        raise Exception("Illegal state")


def p_class_extras_2(p):
    '''
    class_extras_2 : COMA CID class_extras_2
        | PARIZQ vars2 PARDER
    '''
    type = p.slice[1].type
    if type == "PARIZQ":
        p[0] = p[1], p[2], p[3], "SUPERCLASS"
    else:
        arg1, arg2, arg3, type = p[3]
        if type == "SUPERCLASS":
            p[0] = None, [], ClassParent(p[2], arg2), "BOTH"
        elif type == "BOTH":
            p[0] = None, [p[2]] + arg2, arg3, "BOTH"
        else:
            raise Exception("Illegal state")


def p_classparams(p):
    '''
    classparams : PARIZQ classparams2 PARDER
        | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[2]


def p_classparams2(p):
    '''
    classparams2 : vars3 tipo ID classparams3
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [VarDeclaration(p[3], p[2], p[1])] + p[4]


def p_classparams3(p):
    '''
    classparams3 : COMA vars3 tipo ID classparams3
        | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [VarDeclaration(p[4], p[3], p[2])] + p[5]


def p_varcte(p):
    '''
    varcte : ID
    | INTNUM
    | FLOATNUM
    | TRUE
    | FALSE
    | STRINGVAL
    | NULL
    | ID CORCHIZQ varcte CORCHDER
    | ID PUNTO ID varcte_param_fun
    | ID PARIZQ llamada_param PARDER
    '''
    if len(p) == 2:
        type = p.slice[1].type
        p[0] = ConstantVar(p[1], type)
    elif len(p) == 5:
        type = p.slice[2].type
        if type == "PARIZQ":
            p[0] = FunCall(p[1], p[3])
        else:
            if p[4] is None:
                p[0] = ObjectMember(p[1], p[3])
            else:
                p[0] = FunCall(p[3], p[4], p[1])


def p_varcte_param_fun(p):
    '''
    varcte_param_fun : PARIZQ llamada_param PARDER
        | empty
    '''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[2]


def p_expresion(p):
    '''
    expresion : megaexp
    '''
    p[0] = p[1]


def p_expresionr(p):
    '''
    expresionr : COMA expresion expresionr
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[2]] + p[3]


def p_expresion2(p):
    '''
    expresion2 : expresion expresionr
    | empty
    '''


def p_superexp(p):
    '''
    superexp : exp oplog
    '''
    p[0] = RelationalOperation(p[1], p[2])


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
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = RelationalOperand(p[1], p[2])


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
    | obj_call estatuto
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]


def p_asignacion(p):
    '''
    asignacion : ID asignacion3 IGUAL asignacion2 COLON
    '''
    p[0] = Assignment(p[1], p[4])


def p_asignacion2(p):
    '''
    asignacion2 : expresion
    | CORCHDER expresion asignacion2r CORCHIZQ
    | READ PARIZQ assign_read PARDER
    | CID PARIZQ class_call_args expresionr PARDER
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 5:
        p[0] = Read(p[3])
    elif len(p) == 6:
        p[0] = NewObject(p[1], p[3] + p[4])


def p_class_call_args(p):
    '''
    class_call_args : expresion
        | empty
    '''
    if p[1] is None:
        p[0] = []
    else:
        p[0] = [p[1]]


def p_assign_read(p):
    '''
    assign_read : STRINGVAL
        | empty
    '''
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
    condicion : IF condicion2 estatutor
    '''
    base_exp, stmts = p[2]
    p[0] = If(base_exp, stmts, p[3])


def p_condicion2(p):
    '''
    condicion2 : PARIZQ expresion PARDER bloque
    '''
    p[0] = p[2], p[4]


def p_condicionr(p):
    '''
    condicionr : ELSE IF condicion2
    | empty
    '''


def p_bloque(p):
    '''
    bloque : LLAVEIZQ estatuto bloque2 LLAVEDER
    '''
    p[0] = p[2]


def p_bloque2(p):
    '''
    bloque2 : RETURN bloque3
    | empty
    '''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[2]


def p_bloque3(p):
    '''
    bloque3 : expresion COLON
    | empty
    '''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[1]


def p_estatutor(p):
    '''
    estatutor : ELSE bloque
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[2]


def p_escritura(p):
    '''
    escritura : WRITE PARIZQ esc1 esc2 PARDER COLON
    '''
    p[0] = Write(p[3] + p[4])


def p_esc1(p):
    '''
    esc1 : expresion
    | STRING
    '''
    p[0] = [p[1]]


def p_esc2(p):
    '''
    esc2 : COMA esc1 esc2
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[2] + p[3]


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
    | factor2 varcte
    '''
    if p[1] is None:
        p[0] = p[2]
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
        type = p.slice[1].type
        if type == 'POR':
            p[0] = TerminoR(operator.mul, p[2], p[3])
        elif type == 'SOBRE':
            p[0] = TerminoR(operator.floordiv, p[2], p[3])
        else:
            raise Exception("Invalid operator type %s in terminor" % type)


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
        type = p.slice[1].type
        if type == 'MAS':
            p[0] = ExpR(operator.add, p[2], p[3])
        elif type == 'MENOS':
            p[0] = ExpR(operator.sub, p[2], p[3])
        else:
            raise Exception("Invalid operator type %s in expr" % type)


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
        p[0] = None
    else:
        type = p.slice[1].type
        if type == 'MAS':
            p[0] = operator.add
        elif type == 'MENOS':
            p[0] = operator.sub
        else:
            raise Exception("Invalid operator type %s in factor2" % type)


def p_for(p):
    '''
    for : FOR PARIZQ ID IN for2 PARDER bloque
    '''
    p[0] = ForIn(p[3], p[5], p[7])


def p_for2(p):
    '''
    for2 : ID
    | range
    '''
    p[0] = p[1]


def p_range(p):
    '''
    range : INTNUM PUNTOSRANGO INTNUM
        | ID PUNTOSRANGO ID
        | ID PUNTOSRANGO INTNUM
        | INTNUM PUNTOSRANGO ID
    '''
    type = p.slice[1].type
    type2 = p.slice[3].type
    p[0] = Range(ConstantVar(p[1], type), ConstantVar(p[3], type2))


def p_while(p):
    '''
    while : WHILE PARIZQ expresion PARDER bloque
    '''
    p[0] = While(p[3], p[5])


def p_when(p):
    '''
    when : WHEN LLAVEIZQ when2 LLAVEDER
    '''
    p[0] = p[3]


def p_when2(p):
    '''
    when2 : expresion FLECHITA bloque when2
    | ELSE FLECHITA bloque
    | empty
    '''
    if len(p) == 2:
        p[0] = None
    elif len(p) == 4:
        p[0] = WhenBranch(None, p[3], None)
    else:
        p[0] = WhenBranch(p[1], p[3], p[4])


def p_fun(p):
    '''
    fun : vars3 FUN ID PARIZQ fun2 PARDER fun3 funbody
    '''
    body: FunBody = p[8]
    body.params = p[5]
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
    p[0] = FunBody([], p[2], p[3], p[4])


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
    if p[1] is None:
        return []
    else:
        p[0] = p[1]


def p_body(p):
    '''
    body : LLAVEIZQ body2 funr body_main LLAVEDER
        | empty
    '''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = ClassBody(vars=p[2], funs=p[3], main=p[4])


def p_body_main(p):
    '''
    body_main : MAIN PARIZQ PARDER mainbloque
        | empty
    '''
    if len(p) == 2:
        p[0] = None
    else:
        p[0] = p[4]


def p_body2(p):
    '''
    body2 : vars multvarsdecl
    | empty
    '''
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1] + p[2]


def p_mainbloque(p):
    '''
    mainbloque : LLAVEIZQ body2 estatuto LLAVEDER
    '''
    p[0] = Main(p[2], p[3])


def p_multvarsdecl(p):
    '''
    multvarsdecl : vars multvarsdecl
    | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + p[2]


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
    llamada : ID PARIZQ llamada_param PARDER COLON
    | empty
    '''
    p[0] = FunCall(p[1], p[3])


def p_obj_call(p):
    '''
    obj_call : ID PUNTO ID PARIZQ llamada_param PARDER COLON
    | empty
    '''
    p[0] = FunCall(p[3], p[5], p[1])


def p_llamada_param(p):
    '''
    llamada_param : expresion expresionr
        | empty
    '''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]


def p_error(p):
    if p is not None:
        print("Syntax error at line %d, illegal token '%s' found" % (p.lineno, p.value))

    print("Unexpected end of input")


def p_empty(p):
    '''empty : '''


lex.lex()
parser = yacc.yacc(start='file')