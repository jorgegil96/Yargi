
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'fileAND BOOL CID CLASS COLON COMA COMENTARIOS COMILLAS CORCHDER CORCHIZQ DATA DIFERENTE DOSPUNTOS ELSE EOL FALSE FLECHITA FLOAT FLOATNUM FOR FUN GLOBAL ID IF IGUAL IGUALIGUAL IN INT INTNUM LIST LLAVEDER LLAVEIZQ MAIN MAS MAYOROIGUAL MAYORQUE MENOROIGUAL MENORQUE MENOS NULL OR PARDER PARIZQ POR PRIVATE PUNTO PUNTOSRANGO RANGE READ RETURN SOBRE STRING STRINGVAL TRUE WHEN WHILE WRITE\n    file : class classr\n    \n    classr : class classr\n        | empty\n    \n    class : CLASS CID classparams class2 body\n        | DATA CLASS CID classparams\n    \n    class2 : DOSPUNTOS CID PARIZQ vars2 PARDER\n        | empty\n    \n    classparams : PARIZQ classparams2 PARDER\n        | empty\n    \n    classparams2 : vars3 tipo ID classparams3\n    | empty\n    \n    classparams3 : COMA vars3 tipo ID classparams3\n        | empty\n    \n    varcte : ID\n    | INTNUM\n    | FLOATNUM\n    | TRUE\n    | FALSE\n    | STRINGVAL\n    | NULL\n    | ID CORCHIZQ varcte CORCHDER\n    | ID PUNTO ID varcte_param_fun\n    | ID PARIZQ llamada_param PARDER\n    \n    varcte_param_fun : PARIZQ llamada_param PARDER\n        | empty\n    \n    expresion : megaexp\n    \n    expresionr : COMA expresion expresionr\n    | empty\n    \n    expresion2 : expresion expresionr\n    | empty\n    \n    superexp : exp oplog\n    \n    oplog : MAYORQUE exp\n    | MENORQUE exp\n    | DIFERENTE exp\n    | MAYOROIGUAL exp\n    | MENOROIGUAL exp\n    | IGUALIGUAL exp\n    | empty\n    \n    megaexp : superexp megaexpr\n    \n    megaexpr : AND superexp megaexpr\n    | OR superexp megaexpr\n    | empty\n    \n    vars : vars3 tipo vars2 COLON\n    | vars3 tipo LIST vars2 COLON\n    \n    varsr : COMA ID varsr\n    | empty\n    \n    vars2 : ID varsr\n    \n    vars3 : PRIVATE\n    | empty\n    \n    estatuto : asignacion estatuto\n    | condicion estatuto\n    | escritura estatuto\n    | for estatuto\n    | while estatuto\n    | when estatuto\n    | llamada estatuto\n    | obj_call estatuto\n    | empty\n    \n    asignacion : ID asignacion3 IGUAL asignacion2 COLON\n    \n    asignacion2 : expresion\n    | CORCHDER expresion asignacion2r CORCHIZQ\n    | READ PARIZQ assign_read PARDER\n    | CID PARIZQ class_call_args expresionr PARDER\n    \n    class_call_args : expresion\n        | empty\n    \n    assign_read : STRINGVAL\n        | empty\n    \n    asignacion2r : COMA expresion asignacion2r\n    | empty\n    \n    asignacion3 : CORCHIZQ expresion CORCHDER\n    | PUNTO ID\n    | empty\n    \n    condicion : IF condicion2 estatutor\n    \n    condicion2 : PARIZQ expresion PARDER bloque\n    \n    condicionr : ELSE IF condicion2\n    | empty\n    \n    bloque : LLAVEIZQ estatuto bloque2 LLAVEDER\n    \n    bloque2 : RETURN bloque3\n    | empty\n    \n    bloque3 : expresion COLON\n    | empty\n    \n    estatutor : ELSE bloque\n    | empty\n    \n    escritura : WRITE PARIZQ esc1 esc2 PARDER COLON\n    \n    esc1 : expresion\n    | STRING\n    \n    esc2 : COMA esc1 esc2\n    | empty\n    \n    tipo : INT\n    | FLOAT\n    | BOOL\n    | STRING\n    | CID\n    \n    factor : PARIZQ expresion PARDER\n    | factor2 varcte\n    \n    terminor : POR factor terminor\n    | SOBRE factor terminor\n    | empty\n    \n    termino : factor terminor\n    \n    exp : termino expr\n    \n    expr : MAS termino expr\n    | MENOS termino expr\n    | empty\n    \n    varcter : COMA varcte varcter\n    | empty\n    \n    factor2 : MAS\n    | MENOS\n    | empty\n    \n    for : FOR PARIZQ ID IN for2 PARDER bloque\n    \n    for2 : ID\n    | range\n    \n    range : INTNUM PUNTOSRANGO INTNUM\n        | ID PUNTOSRANGO ID\n        | ID PUNTOSRANGO INTNUM\n        | INTNUM PUNTOSRANGO ID\n    \n    while : WHILE PARIZQ expresion PARDER bloque\n    \n    when : WHEN LLAVEIZQ when2 LLAVEDER\n    \n    when2 : expresion FLECHITA bloque when2\n    | ELSE FLECHITA bloque\n    | empty\n    \n    fun : vars3 FUN ID PARIZQ fun2 PARDER fun3 funbody\n    \n    fun2 : tipo ID funparamr\n    | empty\n    \n    funparamr : COMA tipo ID funparamr\n    | empty\n    \n    fun3 : DOSPUNTOS tipo\n    | empty\n    \n    funbody : LLAVEIZQ opc1 opc2 bloque2 LLAVEDER\n    \n    opc1 : vars multvarsdecl\n    | empty\n    \n    opc2 : estatuto\n    | empty\n    \n    body : LLAVEIZQ body2 funr body_main LLAVEDER\n        | empty\n    \n    body_main : MAIN PARIZQ PARDER mainbloque\n        | empty\n    \n    body2 : vars multvarsdecl\n    | empty\n    \n    mainbloque : LLAVEIZQ body2 estatuto LLAVEDER\n    \n    multvarsdecl : vars multvarsdecl\n    | empty\n    \n    funr : fun funr\n    | empty\n    \n    llamada : ID PARIZQ llamada_param PARDER COLON\n    | empty\n    \n    obj_call : ID PUNTO ID PARIZQ llamada_param PARDER COLON\n    | empty\n    \n    llamada_param : expresion expresionr\n        | empty\n    empty : '
    
_lr_action_items = {'CLASS':([0,2,4,5,8,11,13,14,15,17,22,23,25,27,61,67,],[3,3,9,3,-150,-150,-9,-150,-150,-7,-5,-4,-134,-8,-6,-133,]),'DATA':([0,2,5,8,11,13,14,15,17,22,23,25,27,61,67,],[4,4,4,-150,-150,-9,-150,-150,-7,-5,-4,-134,-8,-6,-133,]),'$end':([1,2,5,6,7,8,10,11,13,14,15,17,22,23,25,27,61,67,],[0,-150,-150,-1,-3,-150,-2,-150,-9,-150,-150,-7,-5,-4,-134,-8,-6,-133,]),'CID':([3,9,12,16,19,20,21,24,35,36,37,44,46,51,65,66,70,75,76,80,105,108,131,134,164,165,],[8,14,-150,26,33,-49,-48,-150,-150,-49,33,-150,-49,-150,33,-49,-43,33,-44,-150,33,33,-150,171,-150,-49,]),'PARIZQ':([8,14,26,54,69,98,99,100,101,102,120,122,125,126,128,129,134,135,147,169,170,171,175,178,179,182,183,184,185,186,187,190,191,194,195,198,205,211,226,244,255,258,261,277,297,301,],[12,12,38,68,75,120,125,126,127,128,135,135,135,135,135,135,135,135,205,135,225,226,135,135,135,135,135,135,135,135,135,135,135,135,135,244,135,135,135,135,135,135,135,297,135,-77,]),'DOSPUNTOS':([8,11,13,27,86,],[-150,16,-9,-8,105,]),'LLAVEIZQ':([8,11,13,15,17,27,29,30,31,32,33,61,74,86,103,104,106,132,151,209,214,216,217,284,],[-150,-150,-9,24,-7,-8,-89,-90,-91,-92,-93,-6,80,-150,129,131,-127,-126,208,208,208,208,208,208,]),'PRIVATE':([12,24,34,35,36,41,44,45,46,51,58,70,76,80,130,131,164,287,],[21,21,21,21,-138,21,21,-137,-141,21,-140,-43,-44,21,-121,21,21,-128,]),'PARDER':([12,18,20,39,48,49,50,52,62,64,68,72,75,77,78,81,83,84,87,107,109,120,136,137,138,139,140,141,142,143,153,154,155,156,158,166,172,174,176,177,180,181,188,189,192,193,196,197,198,199,200,201,202,203,204,205,210,212,222,225,226,227,229,230,231,232,233,234,235,236,237,238,239,240,241,244,245,249,250,251,252,263,264,265,266,267,268,269,270,271,272,273,274,275,277,278,282,294,295,296,297,298,299,302,303,305,306,310,311,],[-150,27,-11,-150,61,-150,-10,-13,-47,-46,74,-150,-150,-45,-150,86,-123,-12,-150,-122,-125,-150,173,-150,-149,-26,-150,-150,-150,-150,209,-150,-85,-86,214,-150,227,-148,-28,-39,-42,-31,-38,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-150,248,-88,-124,-150,-150,-94,-150,-150,-150,-32,-33,-34,-35,-36,-37,-150,-150,-150,-150,-150,279,-150,-110,284,-111,293,-66,-67,-150,-64,-65,-27,-40,-41,-101,-102,-96,-97,-150,299,-87,309,-21,-22,-150,-25,-23,-113,-114,-112,-115,311,-24,]),'INT':([12,19,20,21,24,35,36,37,44,46,51,65,66,70,75,76,80,105,108,131,164,165,],[-150,29,-49,-48,-150,-150,-49,29,-150,-49,-150,29,-49,-43,29,-44,-150,29,29,-150,-150,-49,]),'FLOAT':([12,19,20,21,24,35,36,37,44,46,51,65,66,70,75,76,80,105,108,131,164,165,],[-150,30,-49,-48,-150,-150,-49,30,-150,-49,-150,30,-49,-43,30,-44,-150,30,30,-150,-150,-49,]),'BOOL':([12,19,20,21,24,35,36,37,44,46,51,65,66,70,75,76,80,105,108,131,164,165,],[-150,31,-49,-48,-150,-150,-49,31,-150,-49,-150,31,-49,-43,31,-44,-150,31,31,-150,-150,-49,]),'STRING':([12,19,20,21,24,35,36,37,44,46,51,65,66,70,75,76,80,105,108,126,131,164,165,211,],[-150,32,-49,-48,-150,-150,-49,32,-150,-49,-150,32,-49,-43,32,-44,-150,32,32,156,-150,-150,-49,156,]),'FUN':([21,24,34,35,36,41,42,43,44,45,46,58,70,76,130,287,],[-48,-150,-150,-150,-138,-150,-49,57,-150,-137,-141,-140,-43,-44,-121,-128,]),'MAIN':([24,34,35,36,40,41,42,44,45,46,56,58,70,76,130,287,],[-150,-150,-150,-138,54,-150,-143,-150,-137,-141,-142,-140,-43,-44,-121,-128,]),'LLAVEDER':([24,34,35,36,40,41,42,44,45,46,53,55,56,58,70,76,79,80,85,88,89,90,91,92,93,94,95,96,97,110,111,112,113,114,115,116,117,118,124,129,130,131,150,152,159,162,163,164,165,207,208,215,218,219,220,221,223,228,246,247,254,255,256,257,258,259,280,281,286,287,288,290,300,301,304,307,],[-150,-150,-150,-138,-150,-150,-143,-150,-137,-141,67,-136,-142,-140,-43,-44,-135,-150,-150,110,-150,-150,-150,-150,-150,-150,-150,-150,-58,-139,-50,-51,-52,-53,-54,-55,-56,-57,-150,-150,-121,-150,-73,-83,215,-120,-150,-150,-130,-82,-150,-117,-150,-131,-58,-129,-59,-144,-150,-74,-116,-150,-119,287,-150,-79,301,-84,-118,-128,-78,-81,-146,-77,-109,-80,]),'ID':([28,29,30,31,32,33,35,36,38,44,45,46,47,57,58,60,63,70,73,76,80,82,85,89,90,91,92,93,94,95,96,97,120,121,122,124,125,126,127,128,129,131,133,134,135,138,144,145,146,149,150,152,162,163,164,165,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,207,208,211,213,215,220,221,223,226,228,242,243,244,247,254,255,258,261,268,281,283,285,290,297,300,301,304,],[39,-89,-90,-91,-92,-93,-150,-138,49,-150,-137,-141,49,69,-140,49,72,-43,78,-44,-150,87,98,98,98,98,98,98,98,98,98,-145,-150,147,-150,-150,-150,-150,157,-150,-150,-150,166,-150,-150,-108,198,-106,-107,-108,-73,-83,-108,98,-150,-130,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-82,98,-150,250,-117,-145,-129,-59,-150,-144,198,277,-150,-74,-116,-150,-150,-150,-108,-84,302,306,-108,-150,-146,-77,-109,]),'LIST':([29,30,31,32,33,47,],[-89,-90,-91,-92,-93,60,]),'IF':([35,36,44,45,46,58,70,76,80,85,89,90,91,92,93,94,95,96,97,124,131,150,152,163,164,165,207,208,215,220,221,223,228,247,254,281,300,301,304,],[-150,-138,-150,-137,-141,-140,-43,-44,-150,99,99,99,99,99,99,99,99,99,-145,-150,-150,-73,-83,99,-150,-130,-82,99,-117,-145,-129,-59,-144,-74,-116,-84,-146,-77,-109,]),'WRITE':([35,36,44,45,46,58,70,76,80,85,89,90,91,92,93,94,95,96,97,124,131,150,152,163,164,165,207,208,215,220,221,223,228,247,254,281,300,301,304,],[-150,-138,-150,-137,-141,-140,-43,-44,-150,100,100,100,100,100,100,100,100,100,-145,-150,-150,-73,-83,100,-150,-130,-82,100,-117,-145,-129,-59,-144,-74,-116,-84,-146,-77,-109,]),'FOR':([35,36,44,45,46,58,70,76,80,85,89,90,91,92,93,94,95,96,97,124,131,150,152,163,164,165,207,208,215,220,221,223,228,247,254,281,300,301,304,],[-150,-138,-150,-137,-141,-140,-43,-44,-150,101,101,101,101,101,101,101,101,101,-145,-150,-150,-73,-83,101,-150,-130,-82,101,-117,-145,-129,-59,-144,-74,-116,-84,-146,-77,-109,]),'WHILE':([35,36,44,45,46,58,70,76,80,85,89,90,91,92,93,94,95,96,97,124,131,150,152,163,164,165,207,208,215,220,221,223,228,247,254,281,300,301,304,],[-150,-138,-150,-137,-141,-140,-43,-44,-150,102,102,102,102,102,102,102,102,102,-145,-150,-150,-73,-83,102,-150,-130,-82,102,-117,-145,-129,-59,-144,-74,-116,-84,-146,-77,-109,]),'WHEN':([35,36,44,45,46,58,70,76,80,85,89,90,91,92,93,94,95,96,97,124,131,150,152,163,164,165,207,208,215,220,221,223,228,247,254,281,300,301,304,],[-150,-138,-150,-137,-141,-140,-43,-44,-150,103,103,103,103,103,103,103,103,103,-145,-150,-150,-73,-83,103,-150,-130,-82,103,-117,-145,-129,-59,-144,-74,-116,-84,-146,-77,-109,]),'COMA':([39,49,72,78,87,137,139,140,141,142,143,154,155,156,166,177,180,181,188,189,192,193,196,197,198,199,200,201,202,203,204,224,226,227,229,230,231,232,233,234,235,236,237,238,239,240,241,249,266,267,268,270,271,272,273,274,275,277,292,295,296,298,299,311,],[51,63,63,51,108,175,-26,-150,-150,-150,-150,211,-85,-86,108,-39,-42,-31,-38,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,261,-150,-94,175,-150,-150,-32,-33,-34,-35,-36,-37,-150,-150,-150,-150,211,175,-64,-65,-40,-41,-101,-102,-96,-97,-150,261,-21,-22,-25,-23,-24,]),'RETURN':([44,46,58,70,76,89,90,91,92,93,94,95,96,97,111,112,113,114,115,116,117,118,124,131,150,152,163,164,165,207,208,215,218,219,220,221,223,228,246,247,254,281,300,301,304,],[-150,-141,-140,-43,-44,-150,-150,-150,-150,-150,-150,-150,-150,-58,-50,-51,-52,-53,-54,-55,-56,-57,-150,-150,-73,-83,-150,-150,-130,-82,-150,-117,258,-131,-58,-129,-59,-144,258,-74,-116,-84,-146,-77,-109,]),'COLON':([49,59,62,64,71,72,77,139,140,141,142,143,167,168,173,177,180,181,188,189,192,193,196,197,198,199,200,201,202,203,204,227,230,231,232,233,234,235,236,237,238,239,240,241,248,270,271,272,273,274,275,277,279,289,291,293,295,296,298,299,309,311,],[-150,70,-47,-46,76,-150,-45,-26,-150,-150,-150,-150,223,-60,228,-39,-42,-31,-38,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-32,-33,-34,-35,-36,-37,-150,-150,-150,-150,281,-40,-41,-101,-102,-96,-97,-150,300,307,-61,-62,-21,-22,-25,-23,-63,-24,]),'PUNTO':([98,198,],[121,243,]),'CORCHIZQ':([98,139,140,141,142,143,177,180,181,188,189,192,193,196,197,198,199,200,201,202,203,204,224,227,230,231,232,233,234,235,236,237,238,239,240,241,260,262,270,271,272,273,274,275,277,292,295,296,298,299,308,311,],[122,-26,-150,-150,-150,-150,-39,-42,-31,-38,-100,-103,-99,-98,-95,242,-15,-16,-17,-18,-19,-20,-150,-94,-150,-150,-32,-33,-34,-35,-36,-37,-150,-150,-150,-150,291,-69,-40,-41,-101,-102,-96,-97,-150,-150,-21,-22,-25,-23,-68,-24,]),'IGUAL':([98,119,123,147,206,],[-150,134,-72,-71,-70,]),'INTNUM':([120,122,125,126,128,129,134,135,138,144,145,146,149,162,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,211,213,226,242,244,255,258,261,268,283,285,290,297,301,],[-150,-150,-150,-150,-150,-150,-150,-150,-108,199,-106,-107,-108,-108,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,253,-150,199,-150,-150,-150,-150,-108,303,305,-108,-150,-77,]),'FLOATNUM':([120,122,125,126,128,129,134,135,138,144,145,146,149,162,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,211,226,242,244,255,258,261,268,290,297,301,],[-150,-150,-150,-150,-150,-150,-150,-150,-108,200,-106,-107,-108,-108,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,200,-150,-150,-150,-150,-108,-108,-150,-77,]),'TRUE':([120,122,125,126,128,129,134,135,138,144,145,146,149,162,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,211,226,242,244,255,258,261,268,290,297,301,],[-150,-150,-150,-150,-150,-150,-150,-150,-108,201,-106,-107,-108,-108,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,201,-150,-150,-150,-150,-108,-108,-150,-77,]),'FALSE':([120,122,125,126,128,129,134,135,138,144,145,146,149,162,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,211,226,242,244,255,258,261,268,290,297,301,],[-150,-150,-150,-150,-150,-150,-150,-150,-108,202,-106,-107,-108,-108,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,202,-150,-150,-150,-150,-108,-108,-150,-77,]),'STRINGVAL':([120,122,125,126,128,129,134,135,138,144,145,146,149,162,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,211,225,226,242,244,255,258,261,268,290,297,301,],[-150,-150,-150,-150,-150,-150,-150,-150,-108,203,-106,-107,-108,-108,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,264,-150,203,-150,-150,-150,-150,-108,-108,-150,-77,]),'NULL':([120,122,125,126,128,129,134,135,138,144,145,146,149,162,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,211,226,242,244,255,258,261,268,290,297,301,],[-150,-150,-150,-150,-150,-150,-150,-150,-108,204,-106,-107,-108,-108,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,-150,204,-150,-150,-150,-150,-108,-108,-150,-77,]),'MAS':([120,122,125,126,128,129,134,135,142,143,169,175,178,179,182,183,184,185,186,187,190,191,193,194,195,196,197,198,199,200,201,202,203,204,205,211,226,227,238,239,240,241,244,255,258,261,274,275,277,295,296,297,298,299,301,311,],[145,145,145,145,145,145,145,145,190,-150,145,145,145,145,145,145,145,145,145,145,145,145,-99,145,145,-98,-95,-14,-15,-16,-17,-18,-19,-20,145,145,145,-94,190,190,-150,-150,145,145,145,145,-96,-97,-150,-21,-22,145,-25,-23,-77,-24,]),'MENOS':([120,122,125,126,128,129,134,135,142,143,169,175,178,179,182,183,184,185,186,187,190,191,193,194,195,196,197,198,199,200,201,202,203,204,205,211,226,227,238,239,240,241,244,255,258,261,274,275,277,295,296,297,298,299,301,311,],[146,146,146,146,146,146,146,146,191,-150,146,146,146,146,146,146,146,146,146,146,146,146,-99,146,146,-98,-95,-14,-15,-16,-17,-18,-19,-20,146,146,146,-94,191,191,-150,-150,146,146,146,146,-96,-97,-150,-21,-22,146,-25,-23,-77,-24,]),'ELSE':([124,129,247,255,301,],[151,161,-74,161,-77,]),'CORCHDER':([134,139,140,141,142,143,148,177,180,181,188,189,192,193,196,197,198,199,200,201,202,203,204,227,230,231,232,233,234,235,236,237,238,239,240,241,270,271,272,273,274,275,276,277,295,296,298,299,311,],[169,-26,-150,-150,-150,-150,206,-39,-42,-31,-38,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-32,-33,-34,-35,-36,-37,-150,-150,-150,-150,-40,-41,-101,-102,-96,-97,295,-150,-21,-22,-25,-23,-24,]),'READ':([134,],[170,]),'FLECHITA':([139,140,141,142,143,160,161,177,180,181,188,189,192,193,196,197,198,199,200,201,202,203,204,227,230,231,232,233,234,235,236,237,238,239,240,241,270,271,272,273,274,275,277,295,296,298,299,311,],[-26,-150,-150,-150,-150,216,217,-39,-42,-31,-38,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-32,-33,-34,-35,-36,-37,-150,-150,-150,-150,-40,-41,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'AND':([140,141,142,143,181,188,189,192,193,196,197,198,199,200,201,202,203,204,227,230,231,232,233,234,235,236,237,238,239,240,241,272,273,274,275,277,295,296,298,299,311,],[178,-150,-150,-150,-31,-38,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,178,178,-32,-33,-34,-35,-36,-37,-150,-150,-150,-150,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'OR':([140,141,142,143,181,188,189,192,193,196,197,198,199,200,201,202,203,204,227,230,231,232,233,234,235,236,237,238,239,240,241,272,273,274,275,277,295,296,298,299,311,],[179,-150,-150,-150,-31,-38,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,179,179,-32,-33,-34,-35,-36,-37,-150,-150,-150,-150,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'MAYORQUE':([141,142,143,189,192,193,196,197,198,199,200,201,202,203,204,227,238,239,240,241,272,273,274,275,277,295,296,298,299,311,],[182,-150,-150,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-150,-150,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'MENORQUE':([141,142,143,189,192,193,196,197,198,199,200,201,202,203,204,227,238,239,240,241,272,273,274,275,277,295,296,298,299,311,],[183,-150,-150,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-150,-150,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'DIFERENTE':([141,142,143,189,192,193,196,197,198,199,200,201,202,203,204,227,238,239,240,241,272,273,274,275,277,295,296,298,299,311,],[184,-150,-150,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-150,-150,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'MAYOROIGUAL':([141,142,143,189,192,193,196,197,198,199,200,201,202,203,204,227,238,239,240,241,272,273,274,275,277,295,296,298,299,311,],[185,-150,-150,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-150,-150,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'MENOROIGUAL':([141,142,143,189,192,193,196,197,198,199,200,201,202,203,204,227,238,239,240,241,272,273,274,275,277,295,296,298,299,311,],[186,-150,-150,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-150,-150,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'IGUALIGUAL':([141,142,143,189,192,193,196,197,198,199,200,201,202,203,204,227,238,239,240,241,272,273,274,275,277,295,296,298,299,311,],[187,-150,-150,-100,-103,-99,-98,-95,-14,-15,-16,-17,-18,-19,-20,-94,-150,-150,-150,-150,-101,-102,-96,-97,-150,-21,-22,-25,-23,-24,]),'POR':([143,197,198,199,200,201,202,203,204,227,240,241,277,295,296,298,299,311,],[194,-95,-14,-15,-16,-17,-18,-19,-20,-94,194,194,-150,-21,-22,-25,-23,-24,]),'SOBRE':([143,197,198,199,200,201,202,203,204,227,240,241,277,295,296,298,299,311,],[195,-95,-14,-15,-16,-17,-18,-19,-20,-94,195,195,-150,-21,-22,-25,-23,-24,]),'IN':([157,],[213,]),'PUNTOSRANGO':([250,253,],[283,285,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'file':([0,],[1,]),'class':([0,2,5,],[2,5,5,]),'classr':([2,5,],[6,10,]),'empty':([2,5,8,11,12,14,15,24,34,35,39,40,41,44,49,51,72,75,78,80,85,86,87,89,90,91,92,93,94,95,96,98,120,122,124,125,126,128,129,131,134,135,137,140,141,142,143,154,163,164,166,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,208,211,218,224,225,226,229,230,231,238,239,240,241,244,246,249,255,258,261,266,277,292,297,],[7,7,13,17,20,13,25,36,42,46,52,55,42,46,64,66,64,83,52,36,97,106,109,97,97,97,97,97,97,97,97,123,138,149,152,149,149,149,162,165,149,149,176,180,188,192,196,212,220,46,109,149,149,149,149,149,149,149,149,149,149,149,149,149,149,138,97,149,259,262,265,268,176,180,180,192,192,196,196,138,259,212,162,290,149,176,298,262,138,]),'classparams':([8,14,],[11,22,]),'class2':([11,],[15,]),'classparams2':([12,],[18,]),'vars3':([12,24,34,35,41,44,51,80,131,164,],[19,37,43,37,43,37,65,37,37,37,]),'body':([15,],[23,]),'tipo':([19,37,65,75,105,108,],[28,47,73,82,132,133,]),'body2':([24,80,],[34,85,]),'vars':([24,35,44,80,131,164,],[35,44,44,35,164,44,]),'funr':([34,41,],[40,56,]),'fun':([34,41,],[41,41,]),'multvarsdecl':([35,44,164,],[45,58,221,]),'vars2':([38,47,60,],[48,59,71,]),'classparams3':([39,78,],[50,84,]),'body_main':([40,],[53,]),'varsr':([49,72,],[62,77,]),'mainbloque':([74,],[79,]),'fun2':([75,],[81,]),'estatuto':([85,89,90,91,92,93,94,95,96,163,208,],[88,111,112,113,114,115,116,117,118,219,246,]),'asignacion':([85,89,90,91,92,93,94,95,96,163,208,],[89,89,89,89,89,89,89,89,89,89,89,]),'condicion':([85,89,90,91,92,93,94,95,96,163,208,],[90,90,90,90,90,90,90,90,90,90,90,]),'escritura':([85,89,90,91,92,93,94,95,96,163,208,],[91,91,91,91,91,91,91,91,91,91,91,]),'for':([85,89,90,91,92,93,94,95,96,163,208,],[92,92,92,92,92,92,92,92,92,92,92,]),'while':([85,89,90,91,92,93,94,95,96,163,208,],[93,93,93,93,93,93,93,93,93,93,93,]),'when':([85,89,90,91,92,93,94,95,96,163,208,],[94,94,94,94,94,94,94,94,94,94,94,]),'llamada':([85,89,90,91,92,93,94,95,96,163,208,],[95,95,95,95,95,95,95,95,95,95,95,]),'obj_call':([85,89,90,91,92,93,94,95,96,163,208,],[96,96,96,96,96,96,96,96,96,96,96,]),'fun3':([86,],[104,]),'funparamr':([87,166,],[107,222,]),'asignacion3':([98,],[119,]),'condicion2':([99,],[124,]),'funbody':([104,],[130,]),'llamada_param':([120,205,244,297,],[136,245,278,310,]),'expresion':([120,122,125,126,128,129,134,135,169,175,205,211,226,244,255,258,261,297,],[137,148,153,155,158,160,168,172,224,229,137,155,267,137,160,289,292,137,]),'megaexp':([120,122,125,126,128,129,134,135,169,175,205,211,226,244,255,258,261,297,],[139,139,139,139,139,139,139,139,139,139,139,139,139,139,139,139,139,139,]),'superexp':([120,122,125,126,128,129,134,135,169,175,178,179,205,211,226,244,255,258,261,297,],[140,140,140,140,140,140,140,140,140,140,230,231,140,140,140,140,140,140,140,140,]),'exp':([120,122,125,126,128,129,134,135,169,175,178,179,182,183,184,185,186,187,205,211,226,244,255,258,261,297,],[141,141,141,141,141,141,141,141,141,141,141,141,232,233,234,235,236,237,141,141,141,141,141,141,141,141,]),'termino':([120,122,125,126,128,129,134,135,169,175,178,179,182,183,184,185,186,187,190,191,205,211,226,244,255,258,261,297,],[142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,142,238,239,142,142,142,142,142,142,142,142,]),'factor':([120,122,125,126,128,129,134,135,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,211,226,244,255,258,261,297,],[143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,143,240,241,143,143,143,143,143,143,143,143,]),'factor2':([120,122,125,126,128,129,134,135,169,175,178,179,182,183,184,185,186,187,190,191,194,195,205,211,226,244,255,258,261,297,],[144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,144,]),'estatutor':([124,],[150,]),'esc1':([126,211,],[154,249,]),'when2':([129,255,],[159,286,]),'opc1':([131,],[163,]),'asignacion2':([134,],[167,]),'expresionr':([137,229,266,],[174,269,294,]),'megaexpr':([140,230,231,],[177,270,271,]),'oplog':([141,],[181,]),'expr':([142,238,239,],[189,272,273,]),'terminor':([143,240,241,],[193,274,275,]),'varcte':([144,242,],[197,276,]),'bloque':([151,209,214,216,217,284,],[207,247,254,255,256,304,]),'esc2':([154,249,],[210,282,]),'opc2':([163,],[218,]),'for2':([213,],[251,]),'range':([213,],[252,]),'bloque2':([218,246,],[257,280,]),'asignacion2r':([224,292,],[260,308,]),'assign_read':([225,],[263,]),'class_call_args':([226,],[266,]),'bloque3':([258,],[288,]),'varcte_param_fun':([277,],[296,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> file","S'",1,None,None,None),
  ('file -> class classr','file',2,'p_file','parser.py',163),
  ('classr -> class classr','classr',2,'p_classr','parser.py',170),
  ('classr -> empty','classr',1,'p_classr','parser.py',171),
  ('class -> CLASS CID classparams class2 body','class',5,'p_class','parser.py',181),
  ('class -> DATA CLASS CID classparams','class',4,'p_class','parser.py',182),
  ('class2 -> DOSPUNTOS CID PARIZQ vars2 PARDER','class2',5,'p_class2','parser.py',192),
  ('class2 -> empty','class2',1,'p_class2','parser.py',193),
  ('classparams -> PARIZQ classparams2 PARDER','classparams',3,'p_classparams','parser.py',203),
  ('classparams -> empty','classparams',1,'p_classparams','parser.py',204),
  ('classparams2 -> vars3 tipo ID classparams3','classparams2',4,'p_classparams2','parser.py',214),
  ('classparams2 -> empty','classparams2',1,'p_classparams2','parser.py',215),
  ('classparams3 -> COMA vars3 tipo ID classparams3','classparams3',5,'p_classparams3','parser.py',225),
  ('classparams3 -> empty','classparams3',1,'p_classparams3','parser.py',226),
  ('varcte -> ID','varcte',1,'p_varcte','parser.py',236),
  ('varcte -> INTNUM','varcte',1,'p_varcte','parser.py',237),
  ('varcte -> FLOATNUM','varcte',1,'p_varcte','parser.py',238),
  ('varcte -> TRUE','varcte',1,'p_varcte','parser.py',239),
  ('varcte -> FALSE','varcte',1,'p_varcte','parser.py',240),
  ('varcte -> STRINGVAL','varcte',1,'p_varcte','parser.py',241),
  ('varcte -> NULL','varcte',1,'p_varcte','parser.py',242),
  ('varcte -> ID CORCHIZQ varcte CORCHDER','varcte',4,'p_varcte','parser.py',243),
  ('varcte -> ID PUNTO ID varcte_param_fun','varcte',4,'p_varcte','parser.py',244),
  ('varcte -> ID PARIZQ llamada_param PARDER','varcte',4,'p_varcte','parser.py',245),
  ('varcte_param_fun -> PARIZQ llamada_param PARDER','varcte_param_fun',3,'p_varcte_param_fun','parser.py',263),
  ('varcte_param_fun -> empty','varcte_param_fun',1,'p_varcte_param_fun','parser.py',264),
  ('expresion -> megaexp','expresion',1,'p_expresion','parser.py',274),
  ('expresionr -> COMA expresion expresionr','expresionr',3,'p_expresionr','parser.py',281),
  ('expresionr -> empty','expresionr',1,'p_expresionr','parser.py',282),
  ('expresion2 -> expresion expresionr','expresion2',2,'p_expresion2','parser.py',292),
  ('expresion2 -> empty','expresion2',1,'p_expresion2','parser.py',293),
  ('superexp -> exp oplog','superexp',2,'p_superexp','parser.py',299),
  ('oplog -> MAYORQUE exp','oplog',2,'p_oplog','parser.py',306),
  ('oplog -> MENORQUE exp','oplog',2,'p_oplog','parser.py',307),
  ('oplog -> DIFERENTE exp','oplog',2,'p_oplog','parser.py',308),
  ('oplog -> MAYOROIGUAL exp','oplog',2,'p_oplog','parser.py',309),
  ('oplog -> MENOROIGUAL exp','oplog',2,'p_oplog','parser.py',310),
  ('oplog -> IGUALIGUAL exp','oplog',2,'p_oplog','parser.py',311),
  ('oplog -> empty','oplog',1,'p_oplog','parser.py',312),
  ('megaexp -> superexp megaexpr','megaexp',2,'p_megaexp','parser.py',322),
  ('megaexpr -> AND superexp megaexpr','megaexpr',3,'p_megaexpr','parser.py',329),
  ('megaexpr -> OR superexp megaexpr','megaexpr',3,'p_megaexpr','parser.py',330),
  ('megaexpr -> empty','megaexpr',1,'p_megaexpr','parser.py',331),
  ('vars -> vars3 tipo vars2 COLON','vars',4,'p_vars','parser.py',341),
  ('vars -> vars3 tipo LIST vars2 COLON','vars',5,'p_vars','parser.py',342),
  ('varsr -> COMA ID varsr','varsr',3,'p_varsr','parser.py',354),
  ('varsr -> empty','varsr',1,'p_varsr','parser.py',355),
  ('vars2 -> ID varsr','vars2',2,'p_vars2','parser.py',365),
  ('vars3 -> PRIVATE','vars3',1,'p_vars3','parser.py',372),
  ('vars3 -> empty','vars3',1,'p_vars3','parser.py',373),
  ('estatuto -> asignacion estatuto','estatuto',2,'p_estatuto','parser.py',380),
  ('estatuto -> condicion estatuto','estatuto',2,'p_estatuto','parser.py',381),
  ('estatuto -> escritura estatuto','estatuto',2,'p_estatuto','parser.py',382),
  ('estatuto -> for estatuto','estatuto',2,'p_estatuto','parser.py',383),
  ('estatuto -> while estatuto','estatuto',2,'p_estatuto','parser.py',384),
  ('estatuto -> when estatuto','estatuto',2,'p_estatuto','parser.py',385),
  ('estatuto -> llamada estatuto','estatuto',2,'p_estatuto','parser.py',386),
  ('estatuto -> obj_call estatuto','estatuto',2,'p_estatuto','parser.py',387),
  ('estatuto -> empty','estatuto',1,'p_estatuto','parser.py',388),
  ('asignacion -> ID asignacion3 IGUAL asignacion2 COLON','asignacion',5,'p_asignacion','parser.py',398),
  ('asignacion2 -> expresion','asignacion2',1,'p_asignacion2','parser.py',405),
  ('asignacion2 -> CORCHDER expresion asignacion2r CORCHIZQ','asignacion2',4,'p_asignacion2','parser.py',406),
  ('asignacion2 -> READ PARIZQ assign_read PARDER','asignacion2',4,'p_asignacion2','parser.py',407),
  ('asignacion2 -> CID PARIZQ class_call_args expresionr PARDER','asignacion2',5,'p_asignacion2','parser.py',408),
  ('class_call_args -> expresion','class_call_args',1,'p_class_call_args','parser.py',420),
  ('class_call_args -> empty','class_call_args',1,'p_class_call_args','parser.py',421),
  ('assign_read -> STRINGVAL','assign_read',1,'p_assign_read','parser.py',431),
  ('assign_read -> empty','assign_read',1,'p_assign_read','parser.py',432),
  ('asignacion2r -> COMA expresion asignacion2r','asignacion2r',3,'p_asignacion2r','parser.py',439),
  ('asignacion2r -> empty','asignacion2r',1,'p_asignacion2r','parser.py',440),
  ('asignacion3 -> CORCHIZQ expresion CORCHDER','asignacion3',3,'p_asignacion3','parser.py',446),
  ('asignacion3 -> PUNTO ID','asignacion3',2,'p_asignacion3','parser.py',447),
  ('asignacion3 -> empty','asignacion3',1,'p_asignacion3','parser.py',448),
  ('condicion -> IF condicion2 estatutor','condicion',3,'p_condicion','parser.py',454),
  ('condicion2 -> PARIZQ expresion PARDER bloque','condicion2',4,'p_condicion2','parser.py',462),
  ('condicionr -> ELSE IF condicion2','condicionr',3,'p_condicionr','parser.py',469),
  ('condicionr -> empty','condicionr',1,'p_condicionr','parser.py',470),
  ('bloque -> LLAVEIZQ estatuto bloque2 LLAVEDER','bloque',4,'p_bloque','parser.py',476),
  ('bloque2 -> RETURN bloque3','bloque2',2,'p_bloque2','parser.py',483),
  ('bloque2 -> empty','bloque2',1,'p_bloque2','parser.py',484),
  ('bloque3 -> expresion COLON','bloque3',2,'p_bloque3','parser.py',494),
  ('bloque3 -> empty','bloque3',1,'p_bloque3','parser.py',495),
  ('estatutor -> ELSE bloque','estatutor',2,'p_estatutor','parser.py',505),
  ('estatutor -> empty','estatutor',1,'p_estatutor','parser.py',506),
  ('escritura -> WRITE PARIZQ esc1 esc2 PARDER COLON','escritura',6,'p_escritura','parser.py',516),
  ('esc1 -> expresion','esc1',1,'p_esc1','parser.py',523),
  ('esc1 -> STRING','esc1',1,'p_esc1','parser.py',524),
  ('esc2 -> COMA esc1 esc2','esc2',3,'p_esc2','parser.py',531),
  ('esc2 -> empty','esc2',1,'p_esc2','parser.py',532),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',542),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',543),
  ('tipo -> BOOL','tipo',1,'p_tipo','parser.py',544),
  ('tipo -> STRING','tipo',1,'p_tipo','parser.py',545),
  ('tipo -> CID','tipo',1,'p_tipo','parser.py',546),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','parser.py',553),
  ('factor -> factor2 varcte','factor',2,'p_factor','parser.py',554),
  ('terminor -> POR factor terminor','terminor',3,'p_terminor','parser.py',564),
  ('terminor -> SOBRE factor terminor','terminor',3,'p_terminor','parser.py',565),
  ('terminor -> empty','terminor',1,'p_terminor','parser.py',566),
  ('termino -> factor terminor','termino',2,'p_termino','parser.py',582),
  ('exp -> termino expr','exp',2,'p_exp','parser.py',589),
  ('expr -> MAS termino expr','expr',3,'p_expr','parser.py',596),
  ('expr -> MENOS termino expr','expr',3,'p_expr','parser.py',597),
  ('expr -> empty','expr',1,'p_expr','parser.py',598),
  ('varcter -> COMA varcte varcter','varcter',3,'p_varcter','parser.py',614),
  ('varcter -> empty','varcter',1,'p_varcter','parser.py',615),
  ('factor2 -> MAS','factor2',1,'p_factor2','parser.py',621),
  ('factor2 -> MENOS','factor2',1,'p_factor2','parser.py',622),
  ('factor2 -> empty','factor2',1,'p_factor2','parser.py',623),
  ('for -> FOR PARIZQ ID IN for2 PARDER bloque','for',7,'p_for','parser.py',639),
  ('for2 -> ID','for2',1,'p_for2','parser.py',646),
  ('for2 -> range','for2',1,'p_for2','parser.py',647),
  ('range -> INTNUM PUNTOSRANGO INTNUM','range',3,'p_range','parser.py',654),
  ('range -> ID PUNTOSRANGO ID','range',3,'p_range','parser.py',655),
  ('range -> ID PUNTOSRANGO INTNUM','range',3,'p_range','parser.py',656),
  ('range -> INTNUM PUNTOSRANGO ID','range',3,'p_range','parser.py',657),
  ('while -> WHILE PARIZQ expresion PARDER bloque','while',5,'p_while','parser.py',666),
  ('when -> WHEN LLAVEIZQ when2 LLAVEDER','when',4,'p_when','parser.py',673),
  ('when2 -> expresion FLECHITA bloque when2','when2',4,'p_when2','parser.py',680),
  ('when2 -> ELSE FLECHITA bloque','when2',3,'p_when2','parser.py',681),
  ('when2 -> empty','when2',1,'p_when2','parser.py',682),
  ('fun -> vars3 FUN ID PARIZQ fun2 PARDER fun3 funbody','fun',8,'p_fun','parser.py',694),
  ('fun2 -> tipo ID funparamr','fun2',3,'p_fun2','parser.py',703),
  ('fun2 -> empty','fun2',1,'p_fun2','parser.py',704),
  ('funparamr -> COMA tipo ID funparamr','funparamr',4,'p_funparamr','parser.py',714),
  ('funparamr -> empty','funparamr',1,'p_funparamr','parser.py',715),
  ('fun3 -> DOSPUNTOS tipo','fun3',2,'p_fun3','parser.py',725),
  ('fun3 -> empty','fun3',1,'p_fun3','parser.py',726),
  ('funbody -> LLAVEIZQ opc1 opc2 bloque2 LLAVEDER','funbody',5,'p_funbody','parser.py',736),
  ('opc1 -> vars multvarsdecl','opc1',2,'p_opc1','parser.py',743),
  ('opc1 -> empty','opc1',1,'p_opc1','parser.py',744),
  ('opc2 -> estatuto','opc2',1,'p_opc2','parser.py',754),
  ('opc2 -> empty','opc2',1,'p_opc2','parser.py',755),
  ('body -> LLAVEIZQ body2 funr body_main LLAVEDER','body',5,'p_body','parser.py',765),
  ('body -> empty','body',1,'p_body','parser.py',766),
  ('body_main -> MAIN PARIZQ PARDER mainbloque','body_main',4,'p_body_main','parser.py',776),
  ('body_main -> empty','body_main',1,'p_body_main','parser.py',777),
  ('body2 -> vars multvarsdecl','body2',2,'p_body2','parser.py',787),
  ('body2 -> empty','body2',1,'p_body2','parser.py',788),
  ('mainbloque -> LLAVEIZQ body2 estatuto LLAVEDER','mainbloque',4,'p_mainbloque','parser.py',798),
  ('multvarsdecl -> vars multvarsdecl','multvarsdecl',2,'p_multvarsdecl','parser.py',805),
  ('multvarsdecl -> empty','multvarsdecl',1,'p_multvarsdecl','parser.py',806),
  ('funr -> fun funr','funr',2,'p_funr','parser.py',816),
  ('funr -> empty','funr',1,'p_funr','parser.py',817),
  ('llamada -> ID PARIZQ llamada_param PARDER COLON','llamada',5,'p_llamada','parser.py',827),
  ('llamada -> empty','llamada',1,'p_llamada','parser.py',828),
  ('obj_call -> ID PUNTO ID PARIZQ llamada_param PARDER COLON','obj_call',7,'p_obj_call','parser.py',835),
  ('obj_call -> empty','obj_call',1,'p_obj_call','parser.py',836),
  ('llamada_param -> expresion expresionr','llamada_param',2,'p_llamada_param','parser.py',843),
  ('llamada_param -> empty','llamada_param',1,'p_llamada_param','parser.py',844),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',860),
]
