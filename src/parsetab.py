
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'fileAND BOOL CID CLASS COLON COMA COMENTARIOS COMILLAS CORCHDER CORCHIZQ DATA DIFERENTE DOSPUNTOS ELSE EOL FALSE FLECHITA FLOAT FLOATNUM FOR FUN GLOBAL ID IF IGUAL IGUALIGUAL IN INT INTERFACE INTNUM LIST LLAVEDER LLAVEIZQ MAIN MAS MAYOROIGUAL MAYORQUE MENOROIGUAL MENORQUE MENOS NULL OR PARDER PARIZQ POR PRIVATE PUNTO PUNTOSRANGO RANGE READ RETURN SOBRE STRING STRINGVAL TRUE WHEN WHILE WRITE\n    file : interface_r class classr\n    \n    interface_r : INTERFACE CID interface_body interface_r\n        | empty\n    \n    interface_body : LLAVEIZQ interface_fun interface_fun_r LLAVEDER\n    \n    interface_fun : FUN ID PARIZQ fun2 PARDER COLON\n    \n    interface_fun_r : interface_fun interface_fun_r\n        | empty\n    \n    classr : class classr\n        | empty\n    \n    class : CLASS CID classparams class2 body\n        | DATA CLASS CID classparams\n    \n    class2 : DOSPUNTOS class_extras\n        | empty\n    \n    class_extras : CID class_extras_2\n    \n    class_extras_2 : COMA CID class_extras_2\n        | PARIZQ vars2 PARDER\n    \n    class_extras_3 : COMA CID class_parent\n        | PARIZQ vars2 PARDER\n        | empty\n    \n    class_interfaces_r : COMA CID class_interfaces_r\n        | empty\n    \n    class_parent : CID PARIZQ vars2 PARDER\n        | empty\n    \n    classparams : PARIZQ classparams2 PARDER\n        | empty\n    \n    classparams2 : vars3 tipo ID classparams3\n    | empty\n    \n    classparams3 : COMA vars3 tipo ID classparams3\n        | empty\n    \n    varcte : ID\n    | INTNUM\n    | FLOATNUM\n    | TRUE\n    | FALSE\n    | STRINGVAL\n    | NULL\n    | ID CORCHIZQ varcte CORCHDER\n    | ID PUNTO ID varcte_param_fun\n    | ID PARIZQ llamada_param PARDER\n    \n    varcte_param_fun : PARIZQ llamada_param PARDER\n        | empty\n    \n    expresion : megaexp\n    \n    expresionr : COMA expresion expresionr\n    | empty\n    \n    expresion2 : expresion expresionr\n    | empty\n    \n    superexp : exp oplog\n    \n    oplog : MAYORQUE exp\n    | MENORQUE exp\n    | DIFERENTE exp\n    | MAYOROIGUAL exp\n    | MENOROIGUAL exp\n    | IGUALIGUAL exp\n    | empty\n    \n    megaexp : superexp megaexpr\n    \n    megaexpr : AND superexp megaexpr\n    | OR superexp megaexpr\n    | empty\n    \n    vars : vars3 tipo vars2 COLON\n    | vars3 tipo LIST vars2 COLON\n    \n    varsr : COMA ID varsr\n    | empty\n    \n    vars2 : ID varsr\n    \n    vars3 : PRIVATE\n    | empty\n    \n    estatuto : asignacion estatuto\n    | condicion estatuto\n    | escritura estatuto\n    | for estatuto\n    | while estatuto\n    | when estatuto\n    | llamada estatuto\n    | obj_call estatuto\n    | empty\n    \n    asignacion : ID asignacion3 IGUAL asignacion2 COLON\n    \n    asignacion2 : expresion\n    | CORCHDER expresion asignacion2r CORCHIZQ\n    | READ PARIZQ assign_read PARDER\n    | CID PARIZQ class_call_args expresionr PARDER\n    \n    class_call_args : expresion\n        | empty\n    \n    assign_read : STRINGVAL\n        | empty\n    \n    asignacion2r : COMA expresion asignacion2r\n    | empty\n    \n    asignacion3 : CORCHIZQ expresion CORCHDER\n    | PUNTO ID\n    | empty\n    \n    condicion : IF condicion2 estatutor\n    \n    condicion2 : PARIZQ expresion PARDER bloque\n    \n    condicionr : ELSE IF condicion2\n    | empty\n    \n    bloque : LLAVEIZQ estatuto bloque2 LLAVEDER\n    \n    bloque2 : RETURN bloque3\n    | empty\n    \n    bloque3 : expresion COLON\n    | empty\n    \n    estatutor : ELSE bloque\n    | empty\n    \n    escritura : WRITE PARIZQ esc1 esc2 PARDER COLON\n    \n    esc1 : expresion\n    | STRING\n    \n    esc2 : COMA esc1 esc2\n    | empty\n    \n    tipo : INT\n    | FLOAT\n    | BOOL\n    | STRING\n    | CID\n    \n    factor : PARIZQ expresion PARDER\n    | factor2 varcte\n    \n    terminor : POR factor terminor\n    | SOBRE factor terminor\n    | empty\n    \n    termino : factor terminor\n    \n    exp : termino expr\n    \n    expr : MAS termino expr\n    | MENOS termino expr\n    | empty\n    \n    varcter : COMA varcte varcter\n    | empty\n    \n    factor2 : MAS\n    | MENOS\n    | empty\n    \n    for : FOR PARIZQ ID IN for2 PARDER bloque\n    \n    for2 : ID\n    | range\n    \n    range : INTNUM PUNTOSRANGO INTNUM\n        | ID PUNTOSRANGO ID\n        | ID PUNTOSRANGO INTNUM\n        | INTNUM PUNTOSRANGO ID\n    \n    while : WHILE PARIZQ expresion PARDER bloque\n    \n    when : WHEN LLAVEIZQ when2 LLAVEDER\n    \n    when2 : expresion FLECHITA bloque when2\n    | ELSE FLECHITA bloque\n    | empty\n    \n    fun : vars3 FUN ID PARIZQ fun2 PARDER fun3 funbody\n    \n    fun2 : tipo ID funparamr\n    | empty\n    \n    funparamr : COMA tipo ID funparamr\n    | empty\n    \n    fun3 : DOSPUNTOS tipo\n    | empty\n    \n    funbody : LLAVEIZQ opc1 opc2 bloque2 LLAVEDER\n    \n    opc1 : vars multvarsdecl\n    | empty\n    \n    opc2 : estatuto\n    | empty\n    \n    body : LLAVEIZQ body2 funr body_main LLAVEDER\n        | empty\n    \n    body_main : MAIN PARIZQ PARDER mainbloque\n        | empty\n    \n    body2 : vars multvarsdecl\n    | empty\n    \n    mainbloque : LLAVEIZQ body2 estatuto LLAVEDER\n    \n    multvarsdecl : vars multvarsdecl\n    | empty\n    \n    funr : fun funr\n    | empty\n    \n    llamada : ID PARIZQ llamada_param PARDER COLON\n    | empty\n    \n    obj_call : ID PUNTO ID PARIZQ llamada_param PARDER COLON\n    | empty\n    \n    llamada_param : expresion expresionr\n        | empty\n    empty : '
    
_lr_action_items = {'INTERFACE':([0,14,49,],[3,3,-4,]),'CLASS':([0,2,4,5,7,9,12,14,17,19,20,21,24,26,31,36,38,39,41,49,55,86,87,97,],[-166,6,-3,6,13,6,-166,-166,-166,-25,-166,-2,-166,-13,-11,-10,-150,-12,-24,-4,-14,-15,-16,-149,]),'DATA':([0,2,4,5,9,12,14,17,19,20,21,24,26,31,36,38,39,41,49,55,86,87,97,],[-166,7,-3,7,7,-166,-166,-166,-25,-166,-2,-166,-13,-11,-10,-150,-12,-24,-4,-14,-15,-16,-149,]),'$end':([1,5,9,10,11,12,16,17,19,20,24,26,31,36,38,39,41,55,86,87,97,],[0,-166,-166,-1,-9,-166,-8,-166,-25,-166,-166,-13,-11,-10,-150,-12,-24,-14,-15,-16,-149,]),'CID':([3,6,13,18,25,28,29,30,37,50,52,53,54,56,66,68,74,91,92,95,100,106,107,112,135,158,160,190,191,],[8,12,20,-166,40,47,-65,-64,-166,47,-166,-65,47,70,-166,-65,-166,47,-65,47,-59,47,-60,-166,47,-166,196,-166,-65,]),'LLAVEIZQ':([8,12,17,19,24,26,39,41,43,44,45,46,47,55,86,87,105,117,133,134,136,159,177,234,239,241,242,308,],[15,-166,-166,-25,37,-13,-12,-24,-105,-106,-107,-108,-109,-14,-15,-16,112,-166,156,158,-143,-142,233,233,233,233,233,233,]),'PARIZQ':([12,20,35,40,70,79,99,128,129,130,131,132,147,149,152,153,155,156,160,161,173,194,195,196,200,203,204,207,208,209,210,211,212,215,216,219,220,223,230,236,250,268,279,282,285,301,321,325,],[18,18,50,57,57,98,106,147,152,153,154,155,161,161,161,161,161,161,161,161,230,161,249,250,161,161,161,161,161,161,161,161,161,161,161,161,161,268,161,161,161,161,161,161,161,321,161,-93,]),'DOSPUNTOS':([12,17,19,41,117,],[-166,25,-25,-24,135,]),'FUN':([15,22,30,32,37,51,52,53,63,64,65,66,67,68,83,93,100,107,157,311,],[23,23,-64,23,-166,-166,-166,-154,-166,-65,82,-166,-153,-157,-156,-5,-59,-60,-137,-144,]),'PRIVATE':([18,37,51,52,53,63,66,67,68,74,83,100,107,112,157,158,190,311,],[30,30,30,30,-154,30,30,-153,-157,30,-156,-59,-60,30,-137,30,30,-144,]),'PARDER':([18,27,29,50,58,59,61,71,72,73,75,77,88,90,94,96,98,102,106,108,109,110,113,114,115,147,162,163,164,165,166,167,168,169,179,180,181,182,184,197,199,201,202,205,206,213,214,217,218,221,222,223,224,225,226,227,228,229,230,235,237,249,250,251,253,254,255,256,257,258,259,260,261,262,263,264,265,268,269,273,274,275,276,287,288,289,290,291,292,293,294,295,296,297,298,299,301,302,306,318,319,320,321,322,323,326,327,329,330,334,335,],[-166,41,-27,-166,-166,76,-139,87,-166,-26,-29,-166,-63,-62,-138,-141,105,-166,-166,-61,-166,-166,117,-28,-140,-166,198,-166,-165,-42,-166,-166,-166,-166,234,-166,-101,-102,239,251,-164,-44,-55,-58,-47,-54,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-166,272,-104,-166,-166,-110,-166,-166,-166,-48,-49,-50,-51,-52,-53,-166,-166,-166,-166,-166,303,-166,-126,308,-127,317,-82,-83,-166,-80,-81,-43,-56,-57,-117,-118,-112,-113,-166,323,-103,333,-37,-38,-166,-41,-39,-129,-130,-128,-131,335,-40,]),'INT':([18,28,29,30,37,50,52,53,54,66,68,74,91,92,95,100,106,107,112,135,158,190,191,],[-166,43,-65,-64,-166,43,-166,-65,43,-166,-65,-166,43,-65,43,-59,43,-60,-166,43,-166,-166,-65,]),'FLOAT':([18,28,29,30,37,50,52,53,54,66,68,74,91,92,95,100,106,107,112,135,158,190,191,],[-166,44,-65,-64,-166,44,-166,-65,44,-166,-65,-166,44,-65,44,-59,44,-60,-166,44,-166,-166,-65,]),'BOOL':([18,28,29,30,37,50,52,53,54,66,68,74,91,92,95,100,106,107,112,135,158,190,191,],[-166,45,-65,-64,-166,45,-166,-65,45,-166,-65,-166,45,-65,45,-59,45,-60,-166,45,-166,-166,-65,]),'STRING':([18,28,29,30,37,50,52,53,54,66,68,74,91,92,95,100,106,107,112,135,153,158,190,191,236,],[-166,46,-65,-64,-166,46,-166,-65,46,-166,-65,-166,46,-65,46,-59,46,-60,-166,46,182,-166,-166,-65,182,]),'LLAVEDER':([22,32,33,34,37,48,51,52,53,62,63,64,66,67,68,78,80,81,83,93,100,107,111,112,116,118,119,120,121,122,123,124,125,126,127,137,138,139,140,141,142,143,144,145,151,156,157,158,176,178,185,188,189,190,191,232,233,240,243,244,245,246,247,252,270,271,278,279,280,281,282,283,304,305,310,311,312,314,324,325,328,331,],[-166,-166,49,-7,-166,-6,-166,-166,-154,-166,-166,-159,-166,-153,-157,97,-152,-158,-156,-5,-59,-60,-151,-166,-166,137,-166,-166,-166,-166,-166,-166,-166,-166,-74,-155,-66,-67,-68,-69,-70,-71,-72,-73,-166,-166,-137,-166,-89,-99,240,-136,-166,-166,-146,-98,-166,-133,-166,-147,-74,-145,-75,-160,-166,-90,-132,-166,-135,311,-166,-95,325,-100,-134,-144,-94,-97,-162,-93,-125,-96,]),'ID':([23,42,43,44,45,46,47,52,53,57,60,66,67,68,69,82,83,85,89,100,103,104,107,112,116,119,120,121,122,123,124,125,126,127,147,148,149,151,152,153,154,155,156,158,160,161,164,170,171,172,175,176,178,188,189,190,191,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,232,233,236,238,240,245,246,247,250,252,266,267,268,271,278,279,282,285,292,305,307,309,314,321,324,325,328,],[35,58,-105,-106,-107,-108,-109,-166,-154,72,77,-166,-153,-157,72,99,-156,72,102,-59,109,110,-60,-166,128,128,128,128,128,128,128,128,128,-161,-166,173,-166,-166,-166,-166,183,-166,-166,-166,-166,-166,-124,223,-122,-123,-124,-89,-99,-124,128,-166,-146,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-98,128,-166,274,-133,-161,-145,-75,-166,-160,223,301,-166,-90,-132,-166,-166,-166,-124,-100,326,330,-124,-166,-162,-93,-125,]),'MAIN':([37,51,52,53,62,63,64,66,67,68,81,83,100,107,157,311,],[-166,-166,-166,-154,79,-166,-159,-166,-153,-157,-158,-156,-59,-60,-137,-144,]),'COMA':([40,58,70,72,77,102,109,110,163,165,166,167,168,169,180,181,182,202,205,206,213,214,217,218,221,222,223,224,225,226,227,228,229,248,250,251,253,254,255,256,257,258,259,260,261,262,263,264,265,273,290,291,292,294,295,296,297,298,299,301,316,319,320,322,323,335,],[56,74,56,89,95,89,74,95,200,-42,-166,-166,-166,-166,236,-101,-102,-55,-58,-47,-54,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,285,-166,-110,200,-166,-166,-48,-49,-50,-51,-52,-53,-166,-166,-166,-166,236,200,-80,-81,-56,-57,-117,-118,-112,-113,-166,285,-37,-38,-41,-39,-40,]),'LIST':([43,44,45,46,47,69,],[-105,-106,-107,-108,-109,85,]),'IF':([52,53,66,67,68,83,100,107,112,116,119,120,121,122,123,124,125,126,127,151,158,176,178,189,190,191,232,233,240,245,246,247,252,271,278,305,324,325,328,],[-166,-154,-166,-153,-157,-156,-59,-60,-166,129,129,129,129,129,129,129,129,129,-161,-166,-166,-89,-99,129,-166,-146,-98,129,-133,-161,-145,-75,-160,-90,-132,-100,-162,-93,-125,]),'WRITE':([52,53,66,67,68,83,100,107,112,116,119,120,121,122,123,124,125,126,127,151,158,176,178,189,190,191,232,233,240,245,246,247,252,271,278,305,324,325,328,],[-166,-154,-166,-153,-157,-156,-59,-60,-166,130,130,130,130,130,130,130,130,130,-161,-166,-166,-89,-99,130,-166,-146,-98,130,-133,-161,-145,-75,-160,-90,-132,-100,-162,-93,-125,]),'FOR':([52,53,66,67,68,83,100,107,112,116,119,120,121,122,123,124,125,126,127,151,158,176,178,189,190,191,232,233,240,245,246,247,252,271,278,305,324,325,328,],[-166,-154,-166,-153,-157,-156,-59,-60,-166,131,131,131,131,131,131,131,131,131,-161,-166,-166,-89,-99,131,-166,-146,-98,131,-133,-161,-145,-75,-160,-90,-132,-100,-162,-93,-125,]),'WHILE':([52,53,66,67,68,83,100,107,112,116,119,120,121,122,123,124,125,126,127,151,158,176,178,189,190,191,232,233,240,245,246,247,252,271,278,305,324,325,328,],[-166,-154,-166,-153,-157,-156,-59,-60,-166,132,132,132,132,132,132,132,132,132,-161,-166,-166,-89,-99,132,-166,-146,-98,132,-133,-161,-145,-75,-160,-90,-132,-100,-162,-93,-125,]),'WHEN':([52,53,66,67,68,83,100,107,112,116,119,120,121,122,123,124,125,126,127,151,158,176,178,189,190,191,232,233,240,245,246,247,252,271,278,305,324,325,328,],[-166,-154,-166,-153,-157,-156,-59,-60,-166,133,133,133,133,133,133,133,133,133,-161,-166,-166,-89,-99,133,-166,-146,-98,133,-133,-161,-145,-75,-160,-90,-132,-100,-162,-93,-125,]),'RETURN':([66,68,83,100,107,119,120,121,122,123,124,125,126,127,138,139,140,141,142,143,144,145,151,158,176,178,189,190,191,232,233,240,243,244,245,246,247,252,270,271,278,305,324,325,328,],[-166,-157,-156,-59,-60,-166,-166,-166,-166,-166,-166,-166,-166,-74,-66,-67,-68,-69,-70,-71,-72,-73,-166,-166,-89,-99,-166,-166,-146,-98,-166,-133,282,-147,-74,-145,-75,-160,282,-90,-132,-100,-162,-93,-125,]),'COLON':([72,76,84,88,90,101,102,108,165,166,167,168,169,192,193,198,202,205,206,213,214,217,218,221,222,223,224,225,226,227,228,229,251,254,255,256,257,258,259,260,261,262,263,264,265,272,294,295,296,297,298,299,301,303,313,315,317,319,320,322,323,333,335,],[-166,93,100,-63,-62,107,-166,-61,-42,-166,-166,-166,-166,247,-76,252,-55,-58,-47,-54,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-48,-49,-50,-51,-52,-53,-166,-166,-166,-166,305,-56,-57,-117,-118,-112,-113,-166,324,331,-77,-78,-37,-38,-41,-39,-79,-40,]),'PUNTO':([128,223,],[148,267,]),'CORCHIZQ':([128,165,166,167,168,169,202,205,206,213,214,217,218,221,222,223,224,225,226,227,228,229,248,251,254,255,256,257,258,259,260,261,262,263,264,265,284,286,294,295,296,297,298,299,301,316,319,320,322,323,332,335,],[149,-42,-166,-166,-166,-166,-55,-58,-47,-54,-116,-119,-115,-114,-111,266,-31,-32,-33,-34,-35,-36,-166,-110,-166,-166,-48,-49,-50,-51,-52,-53,-166,-166,-166,-166,315,-85,-56,-57,-117,-118,-112,-113,-166,-166,-37,-38,-41,-39,-84,-40,]),'IGUAL':([128,146,150,173,231,],[-166,160,-88,-87,-86,]),'INTNUM':([147,149,152,153,155,156,160,161,164,170,171,172,175,188,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,236,238,250,266,268,279,282,285,292,307,309,314,321,325,],[-166,-166,-166,-166,-166,-166,-166,-166,-124,224,-122,-123,-124,-124,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,277,-166,224,-166,-166,-166,-166,-124,327,329,-124,-166,-93,]),'FLOATNUM':([147,149,152,153,155,156,160,161,164,170,171,172,175,188,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,236,250,266,268,279,282,285,292,314,321,325,],[-166,-166,-166,-166,-166,-166,-166,-166,-124,225,-122,-123,-124,-124,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,225,-166,-166,-166,-166,-124,-124,-166,-93,]),'TRUE':([147,149,152,153,155,156,160,161,164,170,171,172,175,188,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,236,250,266,268,279,282,285,292,314,321,325,],[-166,-166,-166,-166,-166,-166,-166,-166,-124,226,-122,-123,-124,-124,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,226,-166,-166,-166,-166,-124,-124,-166,-93,]),'FALSE':([147,149,152,153,155,156,160,161,164,170,171,172,175,188,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,236,250,266,268,279,282,285,292,314,321,325,],[-166,-166,-166,-166,-166,-166,-166,-166,-124,227,-122,-123,-124,-124,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,227,-166,-166,-166,-166,-124,-124,-166,-93,]),'STRINGVAL':([147,149,152,153,155,156,160,161,164,170,171,172,175,188,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,236,249,250,266,268,279,282,285,292,314,321,325,],[-166,-166,-166,-166,-166,-166,-166,-166,-124,228,-122,-123,-124,-124,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,288,-166,228,-166,-166,-166,-166,-124,-124,-166,-93,]),'NULL':([147,149,152,153,155,156,160,161,164,170,171,172,175,188,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,236,250,266,268,279,282,285,292,314,321,325,],[-166,-166,-166,-166,-166,-166,-166,-166,-124,229,-122,-123,-124,-124,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,-166,229,-166,-166,-166,-166,-124,-124,-166,-93,]),'MAS':([147,149,152,153,155,156,160,161,168,169,194,200,203,204,207,208,209,210,211,212,215,216,218,219,220,221,222,223,224,225,226,227,228,229,230,236,250,251,262,263,264,265,268,279,282,285,298,299,301,319,320,321,322,323,325,335,],[171,171,171,171,171,171,171,171,215,-166,171,171,171,171,171,171,171,171,171,171,171,171,-115,171,171,-114,-111,-30,-31,-32,-33,-34,-35,-36,171,171,171,-110,215,215,-166,-166,171,171,171,171,-112,-113,-166,-37,-38,171,-41,-39,-93,-40,]),'MENOS':([147,149,152,153,155,156,160,161,168,169,194,200,203,204,207,208,209,210,211,212,215,216,218,219,220,221,222,223,224,225,226,227,228,229,230,236,250,251,262,263,264,265,268,279,282,285,298,299,301,319,320,321,322,323,325,335,],[172,172,172,172,172,172,172,172,216,-166,172,172,172,172,172,172,172,172,172,172,172,172,-115,172,172,-114,-111,-30,-31,-32,-33,-34,-35,-36,172,172,172,-110,216,216,-166,-166,172,172,172,172,-112,-113,-166,-37,-38,172,-41,-39,-93,-40,]),'ELSE':([151,156,271,279,325,],[177,187,-90,187,-93,]),'CORCHDER':([160,165,166,167,168,169,174,202,205,206,213,214,217,218,221,222,223,224,225,226,227,228,229,251,254,255,256,257,258,259,260,261,262,263,264,265,294,295,296,297,298,299,300,301,319,320,322,323,335,],[194,-42,-166,-166,-166,-166,231,-55,-58,-47,-54,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-48,-49,-50,-51,-52,-53,-166,-166,-166,-166,-56,-57,-117,-118,-112,-113,319,-166,-37,-38,-41,-39,-40,]),'READ':([160,],[195,]),'FLECHITA':([165,166,167,168,169,186,187,202,205,206,213,214,217,218,221,222,223,224,225,226,227,228,229,251,254,255,256,257,258,259,260,261,262,263,264,265,294,295,296,297,298,299,301,319,320,322,323,335,],[-42,-166,-166,-166,-166,241,242,-55,-58,-47,-54,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-48,-49,-50,-51,-52,-53,-166,-166,-166,-166,-56,-57,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'AND':([166,167,168,169,206,213,214,217,218,221,222,223,224,225,226,227,228,229,251,254,255,256,257,258,259,260,261,262,263,264,265,296,297,298,299,301,319,320,322,323,335,],[203,-166,-166,-166,-47,-54,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,203,203,-48,-49,-50,-51,-52,-53,-166,-166,-166,-166,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'OR':([166,167,168,169,206,213,214,217,218,221,222,223,224,225,226,227,228,229,251,254,255,256,257,258,259,260,261,262,263,264,265,296,297,298,299,301,319,320,322,323,335,],[204,-166,-166,-166,-47,-54,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,204,204,-48,-49,-50,-51,-52,-53,-166,-166,-166,-166,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'MAYORQUE':([167,168,169,214,217,218,221,222,223,224,225,226,227,228,229,251,262,263,264,265,296,297,298,299,301,319,320,322,323,335,],[207,-166,-166,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-166,-166,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'MENORQUE':([167,168,169,214,217,218,221,222,223,224,225,226,227,228,229,251,262,263,264,265,296,297,298,299,301,319,320,322,323,335,],[208,-166,-166,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-166,-166,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'DIFERENTE':([167,168,169,214,217,218,221,222,223,224,225,226,227,228,229,251,262,263,264,265,296,297,298,299,301,319,320,322,323,335,],[209,-166,-166,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-166,-166,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'MAYOROIGUAL':([167,168,169,214,217,218,221,222,223,224,225,226,227,228,229,251,262,263,264,265,296,297,298,299,301,319,320,322,323,335,],[210,-166,-166,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-166,-166,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'MENOROIGUAL':([167,168,169,214,217,218,221,222,223,224,225,226,227,228,229,251,262,263,264,265,296,297,298,299,301,319,320,322,323,335,],[211,-166,-166,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-166,-166,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'IGUALIGUAL':([167,168,169,214,217,218,221,222,223,224,225,226,227,228,229,251,262,263,264,265,296,297,298,299,301,319,320,322,323,335,],[212,-166,-166,-116,-119,-115,-114,-111,-30,-31,-32,-33,-34,-35,-36,-110,-166,-166,-166,-166,-117,-118,-112,-113,-166,-37,-38,-41,-39,-40,]),'POR':([169,222,223,224,225,226,227,228,229,251,264,265,301,319,320,322,323,335,],[219,-111,-30,-31,-32,-33,-34,-35,-36,-110,219,219,-166,-37,-38,-41,-39,-40,]),'SOBRE':([169,222,223,224,225,226,227,228,229,251,264,265,301,319,320,322,323,335,],[220,-111,-30,-31,-32,-33,-34,-35,-36,-110,220,220,-166,-37,-38,-41,-39,-40,]),'IN':([183,],[238,]),'PUNTOSRANGO':([274,277,],[307,309,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'file':([0,],[1,]),'interface_r':([0,14,],[2,21,]),'empty':([0,5,9,12,14,17,18,20,22,24,32,37,50,51,52,58,62,63,66,72,74,77,102,106,109,110,112,116,117,119,120,121,122,123,124,125,126,128,147,149,151,152,153,155,156,158,160,161,163,166,167,168,169,180,189,190,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,233,236,243,248,249,250,253,254,255,262,263,264,265,268,270,273,279,282,285,290,301,316,321,],[4,11,11,19,4,26,29,19,34,38,34,53,61,64,68,75,80,64,68,90,92,96,90,61,75,96,53,127,136,127,127,127,127,127,127,127,127,150,164,175,178,175,175,175,188,191,175,175,201,205,213,217,221,237,245,68,175,175,175,175,175,175,175,175,175,175,175,175,175,175,164,127,175,283,286,289,292,201,205,205,217,217,221,221,164,283,237,188,314,175,201,322,286,164,]),'class':([2,5,9,],[5,9,9,]),'classr':([5,9,],[10,16,]),'interface_body':([8,],[14,]),'classparams':([12,20,],[17,31,]),'interface_fun':([15,22,32,],[22,32,32,]),'class2':([17,],[24,]),'classparams2':([18,],[27,]),'vars3':([18,37,51,52,63,66,74,112,158,190,],[28,54,65,54,65,54,91,54,54,54,]),'interface_fun_r':([22,32,],[33,48,]),'body':([24,],[36,]),'class_extras':([25,],[39,]),'tipo':([28,50,54,91,95,106,135,],[42,60,69,103,104,60,159,]),'body2':([37,112,],[51,116,]),'vars':([37,52,66,112,158,190,],[52,66,66,52,190,66,]),'class_extras_2':([40,70,],[55,86,]),'fun2':([50,106,],[59,113,]),'funr':([51,63,],[62,81,]),'fun':([51,63,],[63,63,]),'multvarsdecl':([52,66,190,],[67,83,246,]),'vars2':([57,69,85,],[71,84,101,]),'classparams3':([58,109,],[73,114,]),'body_main':([62,],[78,]),'varsr':([72,102,],[88,108,]),'funparamr':([77,110,],[94,115,]),'mainbloque':([105,],[111,]),'estatuto':([116,119,120,121,122,123,124,125,126,189,233,],[118,138,139,140,141,142,143,144,145,244,270,]),'asignacion':([116,119,120,121,122,123,124,125,126,189,233,],[119,119,119,119,119,119,119,119,119,119,119,]),'condicion':([116,119,120,121,122,123,124,125,126,189,233,],[120,120,120,120,120,120,120,120,120,120,120,]),'escritura':([116,119,120,121,122,123,124,125,126,189,233,],[121,121,121,121,121,121,121,121,121,121,121,]),'for':([116,119,120,121,122,123,124,125,126,189,233,],[122,122,122,122,122,122,122,122,122,122,122,]),'while':([116,119,120,121,122,123,124,125,126,189,233,],[123,123,123,123,123,123,123,123,123,123,123,]),'when':([116,119,120,121,122,123,124,125,126,189,233,],[124,124,124,124,124,124,124,124,124,124,124,]),'llamada':([116,119,120,121,122,123,124,125,126,189,233,],[125,125,125,125,125,125,125,125,125,125,125,]),'obj_call':([116,119,120,121,122,123,124,125,126,189,233,],[126,126,126,126,126,126,126,126,126,126,126,]),'fun3':([117,],[134,]),'asignacion3':([128,],[146,]),'condicion2':([129,],[151,]),'funbody':([134,],[157,]),'llamada_param':([147,230,268,321,],[162,269,302,334,]),'expresion':([147,149,152,153,155,156,160,161,194,200,230,236,250,268,279,282,285,321,],[163,174,179,181,184,186,193,197,248,253,163,181,291,163,186,313,316,163,]),'megaexp':([147,149,152,153,155,156,160,161,194,200,230,236,250,268,279,282,285,321,],[165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,165,]),'superexp':([147,149,152,153,155,156,160,161,194,200,203,204,230,236,250,268,279,282,285,321,],[166,166,166,166,166,166,166,166,166,166,254,255,166,166,166,166,166,166,166,166,]),'exp':([147,149,152,153,155,156,160,161,194,200,203,204,207,208,209,210,211,212,230,236,250,268,279,282,285,321,],[167,167,167,167,167,167,167,167,167,167,167,167,256,257,258,259,260,261,167,167,167,167,167,167,167,167,]),'termino':([147,149,152,153,155,156,160,161,194,200,203,204,207,208,209,210,211,212,215,216,230,236,250,268,279,282,285,321,],[168,168,168,168,168,168,168,168,168,168,168,168,168,168,168,168,168,168,262,263,168,168,168,168,168,168,168,168,]),'factor':([147,149,152,153,155,156,160,161,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,236,250,268,279,282,285,321,],[169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,169,264,265,169,169,169,169,169,169,169,169,]),'factor2':([147,149,152,153,155,156,160,161,194,200,203,204,207,208,209,210,211,212,215,216,219,220,230,236,250,268,279,282,285,321,],[170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,170,]),'estatutor':([151,],[176,]),'esc1':([153,236,],[180,273,]),'when2':([156,279,],[185,310,]),'opc1':([158,],[189,]),'asignacion2':([160,],[192,]),'expresionr':([163,253,290,],[199,293,318,]),'megaexpr':([166,254,255,],[202,294,295,]),'oplog':([167,],[206,]),'expr':([168,262,263,],[214,296,297,]),'terminor':([169,264,265,],[218,298,299,]),'varcte':([170,266,],[222,300,]),'bloque':([177,234,239,241,242,308,],[232,271,278,279,280,328,]),'esc2':([180,273,],[235,306,]),'opc2':([189,],[243,]),'for2':([238,],[275,]),'range':([238,],[276,]),'bloque2':([243,270,],[281,304,]),'asignacion2r':([248,316,],[284,332,]),'assign_read':([249,],[287,]),'class_call_args':([250,],[290,]),'bloque3':([282,],[312,]),'varcte_param_fun':([301,],[320,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> file","S'",1,None,None,None),
  ('file -> interface_r class classr','file',3,'p_file','parser.py',165),
  ('interface_r -> INTERFACE CID interface_body interface_r','interface_r',4,'p_interface_r','parser.py',172),
  ('interface_r -> empty','interface_r',1,'p_interface_r','parser.py',173),
  ('interface_body -> LLAVEIZQ interface_fun interface_fun_r LLAVEDER','interface_body',4,'p_interface_body','parser.py',183),
  ('interface_fun -> FUN ID PARIZQ fun2 PARDER COLON','interface_fun',6,'p_interface_fun','parser.py',190),
  ('interface_fun_r -> interface_fun interface_fun_r','interface_fun_r',2,'p_interface_fun_r','parser.py',197),
  ('interface_fun_r -> empty','interface_fun_r',1,'p_interface_fun_r','parser.py',198),
  ('classr -> class classr','classr',2,'p_classr','parser.py',208),
  ('classr -> empty','classr',1,'p_classr','parser.py',209),
  ('class -> CLASS CID classparams class2 body','class',5,'p_class','parser.py',219),
  ('class -> DATA CLASS CID classparams','class',4,'p_class','parser.py',220),
  ('class2 -> DOSPUNTOS class_extras','class2',2,'p_class2','parser.py',231),
  ('class2 -> empty','class2',1,'p_class2','parser.py',232),
  ('class_extras -> CID class_extras_2','class_extras',2,'p_class_extras','parser.py',242),
  ('class_extras_2 -> COMA CID class_extras_2','class_extras_2',3,'p_class_extras_2','parser.py',255),
  ('class_extras_2 -> PARIZQ vars2 PARDER','class_extras_2',3,'p_class_extras_2','parser.py',256),
  ('class_extras_3 -> COMA CID class_parent','class_extras_3',3,'p_class_extras_3','parser.py',273),
  ('class_extras_3 -> PARIZQ vars2 PARDER','class_extras_3',3,'p_class_extras_3','parser.py',274),
  ('class_extras_3 -> empty','class_extras_3',1,'p_class_extras_3','parser.py',275),
  ('class_interfaces_r -> COMA CID class_interfaces_r','class_interfaces_r',3,'p_class_interfaces_r','parser.py',285),
  ('class_interfaces_r -> empty','class_interfaces_r',1,'p_class_interfaces_r','parser.py',286),
  ('class_parent -> CID PARIZQ vars2 PARDER','class_parent',4,'p_class_parent','parser.py',296),
  ('class_parent -> empty','class_parent',1,'p_class_parent','parser.py',297),
  ('classparams -> PARIZQ classparams2 PARDER','classparams',3,'p_classparams','parser.py',307),
  ('classparams -> empty','classparams',1,'p_classparams','parser.py',308),
  ('classparams2 -> vars3 tipo ID classparams3','classparams2',4,'p_classparams2','parser.py',318),
  ('classparams2 -> empty','classparams2',1,'p_classparams2','parser.py',319),
  ('classparams3 -> COMA vars3 tipo ID classparams3','classparams3',5,'p_classparams3','parser.py',329),
  ('classparams3 -> empty','classparams3',1,'p_classparams3','parser.py',330),
  ('varcte -> ID','varcte',1,'p_varcte','parser.py',340),
  ('varcte -> INTNUM','varcte',1,'p_varcte','parser.py',341),
  ('varcte -> FLOATNUM','varcte',1,'p_varcte','parser.py',342),
  ('varcte -> TRUE','varcte',1,'p_varcte','parser.py',343),
  ('varcte -> FALSE','varcte',1,'p_varcte','parser.py',344),
  ('varcte -> STRINGVAL','varcte',1,'p_varcte','parser.py',345),
  ('varcte -> NULL','varcte',1,'p_varcte','parser.py',346),
  ('varcte -> ID CORCHIZQ varcte CORCHDER','varcte',4,'p_varcte','parser.py',347),
  ('varcte -> ID PUNTO ID varcte_param_fun','varcte',4,'p_varcte','parser.py',348),
  ('varcte -> ID PARIZQ llamada_param PARDER','varcte',4,'p_varcte','parser.py',349),
  ('varcte_param_fun -> PARIZQ llamada_param PARDER','varcte_param_fun',3,'p_varcte_param_fun','parser.py',367),
  ('varcte_param_fun -> empty','varcte_param_fun',1,'p_varcte_param_fun','parser.py',368),
  ('expresion -> megaexp','expresion',1,'p_expresion','parser.py',378),
  ('expresionr -> COMA expresion expresionr','expresionr',3,'p_expresionr','parser.py',385),
  ('expresionr -> empty','expresionr',1,'p_expresionr','parser.py',386),
  ('expresion2 -> expresion expresionr','expresion2',2,'p_expresion2','parser.py',396),
  ('expresion2 -> empty','expresion2',1,'p_expresion2','parser.py',397),
  ('superexp -> exp oplog','superexp',2,'p_superexp','parser.py',403),
  ('oplog -> MAYORQUE exp','oplog',2,'p_oplog','parser.py',410),
  ('oplog -> MENORQUE exp','oplog',2,'p_oplog','parser.py',411),
  ('oplog -> DIFERENTE exp','oplog',2,'p_oplog','parser.py',412),
  ('oplog -> MAYOROIGUAL exp','oplog',2,'p_oplog','parser.py',413),
  ('oplog -> MENOROIGUAL exp','oplog',2,'p_oplog','parser.py',414),
  ('oplog -> IGUALIGUAL exp','oplog',2,'p_oplog','parser.py',415),
  ('oplog -> empty','oplog',1,'p_oplog','parser.py',416),
  ('megaexp -> superexp megaexpr','megaexp',2,'p_megaexp','parser.py',426),
  ('megaexpr -> AND superexp megaexpr','megaexpr',3,'p_megaexpr','parser.py',433),
  ('megaexpr -> OR superexp megaexpr','megaexpr',3,'p_megaexpr','parser.py',434),
  ('megaexpr -> empty','megaexpr',1,'p_megaexpr','parser.py',435),
  ('vars -> vars3 tipo vars2 COLON','vars',4,'p_vars','parser.py',445),
  ('vars -> vars3 tipo LIST vars2 COLON','vars',5,'p_vars','parser.py',446),
  ('varsr -> COMA ID varsr','varsr',3,'p_varsr','parser.py',458),
  ('varsr -> empty','varsr',1,'p_varsr','parser.py',459),
  ('vars2 -> ID varsr','vars2',2,'p_vars2','parser.py',469),
  ('vars3 -> PRIVATE','vars3',1,'p_vars3','parser.py',476),
  ('vars3 -> empty','vars3',1,'p_vars3','parser.py',477),
  ('estatuto -> asignacion estatuto','estatuto',2,'p_estatuto','parser.py',484),
  ('estatuto -> condicion estatuto','estatuto',2,'p_estatuto','parser.py',485),
  ('estatuto -> escritura estatuto','estatuto',2,'p_estatuto','parser.py',486),
  ('estatuto -> for estatuto','estatuto',2,'p_estatuto','parser.py',487),
  ('estatuto -> while estatuto','estatuto',2,'p_estatuto','parser.py',488),
  ('estatuto -> when estatuto','estatuto',2,'p_estatuto','parser.py',489),
  ('estatuto -> llamada estatuto','estatuto',2,'p_estatuto','parser.py',490),
  ('estatuto -> obj_call estatuto','estatuto',2,'p_estatuto','parser.py',491),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',492),
  ('asignacion -> ID asignacion3 IGUAL asignacion2 COLON','asignacion',5,'p_asignacion','parser.py',502),
  ('asignacion2 -> expresion','asignacion2',1,'p_asignacion2','parser.py',509),
  ('asignacion2 -> CORCHDER expresion asignacion2r CORCHIZQ','asignacion2',4,'p_asignacion2','parser.py',510),
  ('asignacion2 -> READ PARIZQ assign_read PARDER','asignacion2',4,'p_asignacion2','parser.py',511),
  ('asignacion2 -> CID PARIZQ class_call_args expresionr PARDER','asignacion2',5,'p_asignacion2','parser.py',512),
  ('class_call_args -> expresion','class_call_args',1,'p_class_call_args','parser.py',524),
  ('class_call_args -> empty','class_call_args',1,'p_class_call_args','parser.py',525),
  ('assign_read -> STRINGVAL','assign_read',1,'p_assign_read','parser.py',535),
  ('assign_read -> empty','assign_read',1,'p_assign_read','parser.py',536),
  ('asignacion2r -> COMA expresion asignacion2r','asignacion2r',3,'p_asignacion2r','parser.py',543),
  ('asignacion2r -> empty','asignacion2r',1,'p_asignacion2r','parser.py',544),
  ('asignacion3 -> CORCHIZQ expresion CORCHDER','asignacion3',3,'p_asignacion3','parser.py',550),
  ('asignacion3 -> PUNTO ID','asignacion3',2,'p_asignacion3','parser.py',551),
  ('asignacion3 -> empty','asignacion3',1,'p_asignacion3','parser.py',552),
  ('condicion -> IF condicion2 estatutor','condicion',3,'p_condicion','parser.py',558),
  ('condicion2 -> PARIZQ expresion PARDER bloque','condicion2',4,'p_condicion2','parser.py',566),
  ('condicionr -> ELSE IF condicion2','condicionr',3,'p_condicionr','parser.py',573),
  ('condicionr -> empty','condicionr',1,'p_condicionr','parser.py',574),
  ('bloque -> LLAVEIZQ estatuto bloque2 LLAVEDER','bloque',4,'p_bloque','parser.py',580),
  ('bloque2 -> RETURN bloque3','bloque2',2,'p_bloque2','parser.py',587),
  ('bloque2 -> empty','bloque2',1,'p_bloque2','parser.py',588),
  ('bloque3 -> expresion COLON','bloque3',2,'p_bloque3','parser.py',598),
  ('bloque3 -> empty','bloque3',1,'p_bloque3','parser.py',599),
  ('estatutor -> ELSE bloque','estatutor',2,'p_estatutor','parser.py',609),
  ('estatutor -> empty','estatutor',1,'p_estatutor','parser.py',610),
  ('escritura -> WRITE PARIZQ esc1 esc2 PARDER COLON','escritura',6,'p_escritura','parser.py',620),
  ('esc1 -> expresion','esc1',1,'p_esc1','parser.py',627),
  ('esc1 -> STRING','esc1',1,'p_esc1','parser.py',628),
  ('esc2 -> COMA esc1 esc2','esc2',3,'p_esc2','parser.py',635),
  ('esc2 -> empty','esc2',1,'p_esc2','parser.py',636),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',646),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',647),
  ('tipo -> BOOL','tipo',1,'p_tipo','parser.py',648),
  ('tipo -> STRING','tipo',1,'p_tipo','parser.py',649),
  ('tipo -> CID','tipo',1,'p_tipo','parser.py',650),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','parser.py',657),
  ('factor -> factor2 varcte','factor',2,'p_factor','parser.py',658),
  ('terminor -> POR factor terminor','terminor',3,'p_terminor','parser.py',668),
  ('terminor -> SOBRE factor terminor','terminor',3,'p_terminor','parser.py',669),
  ('terminor -> empty','terminor',1,'p_terminor','parser.py',670),
  ('termino -> factor terminor','termino',2,'p_termino','parser.py',686),
  ('exp -> termino expr','exp',2,'p_exp','parser.py',693),
  ('expr -> MAS termino expr','expr',3,'p_expr','parser.py',700),
  ('expr -> MENOS termino expr','expr',3,'p_expr','parser.py',701),
  ('expr -> empty','expr',1,'p_expr','parser.py',702),
  ('varcter -> COMA varcte varcter','varcter',3,'p_varcter','parser.py',718),
  ('varcter -> empty','varcter',1,'p_varcter','parser.py',719),
  ('factor2 -> MAS','factor2',1,'p_factor2','parser.py',725),
  ('factor2 -> MENOS','factor2',1,'p_factor2','parser.py',726),
  ('factor2 -> empty','factor2',1,'p_factor2','parser.py',727),
  ('for -> FOR PARIZQ ID IN for2 PARDER bloque','for',7,'p_for','parser.py',743),
  ('for2 -> ID','for2',1,'p_for2','parser.py',750),
  ('for2 -> range','for2',1,'p_for2','parser.py',751),
  ('range -> INTNUM PUNTOSRANGO INTNUM','range',3,'p_range','parser.py',758),
  ('range -> ID PUNTOSRANGO ID','range',3,'p_range','parser.py',759),
  ('range -> ID PUNTOSRANGO INTNUM','range',3,'p_range','parser.py',760),
  ('range -> INTNUM PUNTOSRANGO ID','range',3,'p_range','parser.py',761),
  ('while -> WHILE PARIZQ expresion PARDER bloque','while',5,'p_while','parser.py',770),
  ('when -> WHEN LLAVEIZQ when2 LLAVEDER','when',4,'p_when','parser.py',777),
  ('when2 -> expresion FLECHITA bloque when2','when2',4,'p_when2','parser.py',784),
  ('when2 -> ELSE FLECHITA bloque','when2',3,'p_when2','parser.py',785),
  ('when2 -> empty','when2',1,'p_when2','parser.py',786),
  ('fun -> vars3 FUN ID PARIZQ fun2 PARDER fun3 funbody','fun',8,'p_fun','parser.py',798),
  ('fun2 -> tipo ID funparamr','fun2',3,'p_fun2','parser.py',807),
  ('fun2 -> empty','fun2',1,'p_fun2','parser.py',808),
  ('funparamr -> COMA tipo ID funparamr','funparamr',4,'p_funparamr','parser.py',818),
  ('funparamr -> empty','funparamr',1,'p_funparamr','parser.py',819),
  ('fun3 -> DOSPUNTOS tipo','fun3',2,'p_fun3','parser.py',829),
  ('fun3 -> empty','fun3',1,'p_fun3','parser.py',830),
  ('funbody -> LLAVEIZQ opc1 opc2 bloque2 LLAVEDER','funbody',5,'p_funbody','parser.py',840),
  ('opc1 -> vars multvarsdecl','opc1',2,'p_opc1','parser.py',847),
  ('opc1 -> empty','opc1',1,'p_opc1','parser.py',848),
  ('opc2 -> estatuto','opc2',1,'p_opc2','parser.py',858),
  ('opc2 -> empty','opc2',1,'p_opc2','parser.py',859),
  ('body -> LLAVEIZQ body2 funr body_main LLAVEDER','body',5,'p_body','parser.py',869),
  ('body -> empty','body',1,'p_body','parser.py',870),
  ('body_main -> MAIN PARIZQ PARDER mainbloque','body_main',4,'p_body_main','parser.py',880),
  ('body_main -> empty','body_main',1,'p_body_main','parser.py',881),
  ('body2 -> vars multvarsdecl','body2',2,'p_body2','parser.py',891),
  ('body2 -> empty','body2',1,'p_body2','parser.py',892),
  ('mainbloque -> LLAVEIZQ body2 estatuto LLAVEDER','mainbloque',4,'p_mainbloque','parser.py',902),
  ('multvarsdecl -> vars multvarsdecl','multvarsdecl',2,'p_multvarsdecl','parser.py',909),
  ('multvarsdecl -> empty','multvarsdecl',1,'p_multvarsdecl','parser.py',910),
  ('funr -> fun funr','funr',2,'p_funr','parser.py',920),
  ('funr -> empty','funr',1,'p_funr','parser.py',921),
  ('llamada -> ID PARIZQ llamada_param PARDER COLON','llamada',5,'p_llamada','parser.py',931),
  ('llamada -> empty','llamada',1,'p_llamada','parser.py',932),
  ('obj_call -> ID PUNTO ID PARIZQ llamada_param PARDER COLON','obj_call',7,'p_obj_call','parser.py',939),
  ('obj_call -> empty','obj_call',1,'p_obj_call','parser.py',940),
  ('llamada_param -> expresion expresionr','llamada_param',2,'p_llamada_param','parser.py',947),
  ('llamada_param -> empty','llamada_param',1,'p_llamada_param','parser.py',948),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',964),
]
