
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'classAND BOOL BOOLVAL CID CLASS COLON COMA COMENTARIOS COMILLAS CORCHDER CORCHIZQ DIFERENTE DOSPUNTOS ELSE EOL FLECHITA FLOAT FLOATNUM FOR FUN GLOBAL ID IF IGUAL IGUALIGUAL IN INT INTNUM LIST LLAVEDER LLAVEIZQ MAIN MAS MAYOROIGUAL MAYORQUE MENOROIGUAL MENORQUE MENOS OR PARDER PARIZQ POR PRIVATE PUNTO PUNTOSRANGO RANGE READ RETURN SOBRE STRING STRING WHEN WHILE WRITE\n    resultado : class\n    \n    class : CLASS CID classparams class2 body\n    \n    class2 : DOSPUNTOS ID PARIZQ vars2 PARDER\n    | empty\n    \n    classparams : PARIZQ classparams2 PARDER\n    \n    classparams2 : vars\n    | empty\n    \n    bloque : LLAVEIZQ estatuto bloque2 LLAVEDER\n    \n    bloque2 : RETURN bloque3\n    | empty\n    \n    bloque3 : expresion\n    | empty\n    \n    varcte : ID\n    | INTNUM\n    | FLOATNUM\n    | BOOLVAL\n    | STRING\n    | ID CORCHIZQ varcte CORCHDER\n    | ID PUNTO ID\n    | ID PARIZQ expresion2 PARDER\n    \n    expresion : megaexp\n    | ID PARIZQ expresion2 PARDER\n   \n    expresionr : COMA expresion expresionr\n    | empty\n    \n    expresion2 : expresion expresionr\n    | empty\n    \n    oplog : MAYORQUE exp\n    | MENORQUE exp\n    | DIFERENTE exp\n    | MAYOROIGUAL exp\n    | MENOROIGUAL exp\n    | IGUALIGUAL exp\n    | empty\n    \n    superexp : exp oplog\n    \n    megaexp : superexp megaexpr\n    \n    megaexpr : AND superexp megaexpr\n    | OR superexp megaexpr\n    | empty\n    \n    vars : vars3 tipo vars2 COLON\n    | vars3 tipo LIST vars2 COLON\n    \n    varsr : COMA ID varsr\n    | empty\n    \n    vars2 : ID varsr\n    \n    vars3 : PRIVATE\n    | empty\n    \n    estatuto : asignacion estatuto\n    | condicion estatuto\n    | escritura estatuto\n    | for estatuto\n    | while estatuto\n    | when estatuto\n    | llamada estatuto\n    | empty\n    \n    asignacion : ID asignacion3 IGUAL asignacion2 COLON\n    \n    asignacion2 : expresion\n    | CORCHDER expresion asignacion2r CORCHIZQ\n    | READ PARIZQ STRING PARDER\n    \n    asignacion2r : COMA expresion asignacion2r\n    | empty\n    \n    asignacion3 : CORCHIZQ expresion CORCHDER\n    | PUNTO ID\n    | empty\n    \n    condicion : IF condicion2 condicionr estatutor\n    \n    condicion2 : PARIZQ expresion PARDER bloque\n    \n    condicionr : ELSE IF condicion2\n    | empty\n    \n    estatutor : ELSE bloque\n    | empty\n    \n    escritura : WRITE PARIZQ esc1 esc2 PARDER\n    \n    esc1 : expresion\n    | STRING\n    \n    esc2 : COMA esc1 esc2\n    | empty\n    \n    tipo : INT\n    | FLOAT\n    | BOOL\n    | STRING\n    | CID\n    \n    factor : PARIZQ expresion PARDER\n    | factor2 varcte varcter\n    \n    terminor : POR factor terminor\n    | SOBRE factor terminor\n    | empty\n    \n    termino : factor terminor\n    \n    exp : termino expr\n    \n    expr : MAS termino expr\n    | MENOS termino expr\n    | empty\n    \n    varcter : COMA varcte varcter\n    | empty\n    \n    factor2 : MAS\n    | MENOS\n    | empty\n    \n    for : FOR PARIZQ ID IN for2 PARDER bloque\n    \n    for2 : ID\n    | range\n    \n    range : INTNUM PUNTOSRANGO INTNUM\n    \n    while : WHILE PARIZQ expresion PARDER bloque\n    \n    when : WHEN PARIZQ expresion PARDER LLAVEIZQ when2 LLAVEDER\n    \n    when2 : varcte varcter FLECHITA bloque when2\n    | IN range FLECHITA bloque when2\n    | ELSE FLECHITA bloque when2\n    | empty\n    \n    fun : vars3 FUN ID PARIZQ fun2 PARDER fun3 funbody\n    \n    fun2 : tipo ID funparamr\n    | empty\n    \n    funparamr : COMA tipo ID funparamr\n    | empty\n    \n    fun3 : DOSPUNTOS tipo\n    | empty\n    \n    funbody : LLAVEIZQ opc1 opc2 bloque2 LLAVEDER\n    \n    opc1 : vars multvarsdecl\n    | empty\n    \n    opc2 : estatuto\n    | empty\n    \n    body : LLAVEIZQ body2 funr MAIN PARIZQ PARDER bloque LLAVEDER\n    \n    body2 : vars multvarsdecl\n    | empty\n    \n    multvarsdecl : vars\n    | empty\n    \n    funr : fun funr\n    | empty\n    \n    llamada : ID PARIZQ expresion expresionr PARDER\n    | empty\n    empty : '
    
_lr_action_items = {'CLASS':([0,],[2,]),'$end':([1,14,75,],[0,-2,-116,]),'CID':([2,5,11,12,13,15,25,26,37,39,48,54,100,103,135,186,187,],[3,-125,-45,23,-44,-125,-125,-45,-45,-39,-40,23,23,23,-125,-125,-45,]),'PARIZQ':([3,16,44,51,69,70,71,72,73,74,79,89,90,94,95,97,98,110,111,119,138,141,142,145,146,147,148,149,150,153,154,157,158,161,168,169,171,177,180,210,245,],[5,27,50,54,89,94,95,96,97,98,111,111,111,111,111,111,111,138,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,210,111,213,111,94,111,111,111,]),'DOSPUNTOS':([4,17,76,],[7,-5,100,]),'LLAVEIZQ':([4,6,8,17,19,20,21,22,23,47,53,76,99,101,136,175,178,183,184,250,269,272,273,],[-125,15,-4,-5,-74,-75,-76,-77,-78,-3,55,-125,135,-110,-109,55,55,55,226,55,55,55,55,]),'PARDER':([5,9,10,11,30,38,39,41,43,48,49,50,52,54,57,59,77,102,104,109,112,113,114,115,120,127,128,129,130,132,133,138,139,140,143,144,151,152,155,156,159,160,161,162,163,164,165,170,172,179,181,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,207,210,215,220,221,222,223,231,232,233,234,235,236,237,238,239,240,242,243,247,248,249,258,259,260,265,],[-125,17,-6,-7,-125,47,-39,-43,-42,-40,-125,53,-41,-125,76,-106,-125,-105,-108,-21,-125,-125,-125,-125,-125,178,-125,-70,-71,183,184,-125,192,-35,-38,-34,-33,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,214,-24,219,-73,-125,232,-125,-26,-79,-125,-125,-27,-28,-29,-30,-31,-32,-125,-125,-125,-125,-80,-90,-125,-125,-125,-95,250,-96,-107,-22,-25,-36,-37,-86,-87,-81,-82,-125,-19,260,263,-23,-72,-89,-18,-20,-97,]),'INT':([5,11,12,13,15,25,26,37,39,48,54,100,103,135,186,187,],[-125,-45,19,-44,-125,-125,-45,-45,-39,-40,19,19,19,-125,-125,-45,]),'FLOAT':([5,11,12,13,15,25,26,37,39,48,54,100,103,135,186,187,],[-125,-45,20,-44,-125,-125,-45,-45,-39,-40,20,20,20,-125,-125,-45,]),'BOOL':([5,11,12,13,15,25,26,37,39,48,54,100,103,135,186,187,],[-125,-45,21,-44,-125,-125,-45,-45,-39,-40,21,21,21,-125,-125,-45,]),'STRING':([5,11,12,13,15,25,26,37,39,48,54,79,89,90,94,95,97,98,100,103,105,108,111,116,117,118,119,121,135,138,141,142,145,146,147,148,149,150,153,154,157,158,168,171,180,186,187,191,206,208,210,213,226,245,274,275,276,],[-125,-45,22,-44,-125,-125,-45,-45,-39,-40,22,-125,-125,-125,-125,130,-125,-125,22,22,-8,-93,-125,165,-91,-92,-125,-93,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,130,-125,-45,-93,165,165,-125,247,165,-125,165,165,165,]),'PRIVATE':([5,15,24,25,26,32,35,36,37,39,48,134,135,186,270,],[13,13,13,13,-118,13,-119,-117,-120,-39,-40,-104,13,13,-111,]),'ID':([7,18,19,20,21,22,23,27,29,35,37,39,42,46,48,55,58,61,62,63,64,65,66,67,68,79,89,90,91,93,94,95,96,97,98,105,108,111,116,117,118,119,121,124,126,135,137,138,141,142,145,146,147,148,149,150,153,154,157,158,168,171,174,176,180,182,185,186,187,191,206,208,209,210,211,214,216,217,218,219,225,226,229,230,245,264,266,274,275,276,],[16,30,-74,-75,-76,-77,-78,30,30,-119,-120,-39,49,51,-40,69,77,69,69,69,69,69,69,69,-124,110,110,110,123,-125,110,110,131,110,110,-8,-93,110,161,-91,-92,110,-93,-125,-66,-125,188,110,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,110,110,-63,-68,110,221,69,-125,-113,-93,161,161,242,110,-54,-123,-67,-65,-64,-69,-98,161,-124,-112,110,-94,-99,161,161,161,]),'FUN':([13,15,24,25,26,32,33,34,35,36,37,39,48,134,270,],[-44,-125,-125,-125,-118,-125,-45,46,-119,-117,-120,-39,-40,-104,-111,]),'MAIN':([15,24,25,26,31,32,33,35,36,37,39,45,48,134,270,],[-125,-125,-125,-118,44,-125,-122,-119,-117,-120,-39,-121,-40,-104,-111,]),'LIST':([18,19,20,21,22,23,],[29,-74,-75,-76,-77,-78,]),'COLON':([28,30,40,41,43,49,52,109,112,113,114,115,140,143,144,151,152,155,156,159,160,161,162,163,164,165,166,167,192,193,194,195,196,197,198,199,200,201,202,203,204,205,207,232,234,235,236,237,238,239,240,242,258,259,260,261,263,],[39,-125,48,-43,-42,-125,-41,-21,-125,-125,-125,-125,-35,-38,-34,-33,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,211,-55,-79,-125,-125,-27,-28,-29,-30,-31,-32,-125,-125,-125,-125,-80,-90,-22,-36,-37,-86,-87,-81,-82,-125,-19,-89,-18,-20,-56,-57,]),'COMA':([30,49,77,109,112,113,114,115,120,128,129,130,140,143,144,151,152,155,156,159,160,161,162,163,164,165,188,190,192,193,194,195,196,197,198,199,200,201,202,203,204,205,207,212,215,220,232,234,235,236,237,238,239,240,242,253,258,259,260,262,],[42,42,103,-21,-125,-125,-125,-125,171,180,-70,-71,-35,-38,-34,-33,-85,-88,-84,-83,206,-13,-14,-15,-16,-17,103,171,-79,-125,-125,-27,-28,-29,-30,-31,-32,-125,-125,-125,-125,-80,-90,245,171,180,-22,-36,-37,-86,-87,-81,-82,206,-19,206,-89,-18,-20,245,]),'IF':([35,37,39,48,55,61,62,63,64,65,66,67,68,93,105,124,125,126,135,174,176,185,186,187,211,214,216,217,218,219,225,229,230,264,266,],[-119,-120,-39,-40,70,70,70,70,70,70,70,70,-124,-125,-8,-125,177,-66,-125,-63,-68,70,-125,-113,-54,-123,-67,-65,-64,-69,-98,-124,-112,-94,-99,]),'WRITE':([35,37,39,48,55,61,62,63,64,65,66,67,68,93,105,124,126,135,174,176,185,186,187,211,214,216,217,218,219,225,229,230,264,266,],[-119,-120,-39,-40,71,71,71,71,71,71,71,71,-124,-125,-8,-125,-66,-125,-63,-68,71,-125,-113,-54,-123,-67,-65,-64,-69,-98,-124,-112,-94,-99,]),'FOR':([35,37,39,48,55,61,62,63,64,65,66,67,68,93,105,124,126,135,174,176,185,186,187,211,214,216,217,218,219,225,229,230,264,266,],[-119,-120,-39,-40,72,72,72,72,72,72,72,72,-124,-125,-8,-125,-66,-125,-63,-68,72,-125,-113,-54,-123,-67,-65,-64,-69,-98,-124,-112,-94,-99,]),'WHILE':([35,37,39,48,55,61,62,63,64,65,66,67,68,93,105,124,126,135,174,176,185,186,187,211,214,216,217,218,219,225,229,230,264,266,],[-119,-120,-39,-40,73,73,73,73,73,73,73,73,-124,-125,-8,-125,-66,-125,-63,-68,73,-125,-113,-54,-123,-67,-65,-64,-69,-98,-124,-112,-94,-99,]),'WHEN':([35,37,39,48,55,61,62,63,64,65,66,67,68,93,105,124,126,135,174,176,185,186,187,211,214,216,217,218,219,225,229,230,264,266,],[-119,-120,-39,-40,74,74,74,74,74,74,74,74,-124,-125,-8,-125,-66,-125,-63,-68,74,-125,-113,-54,-123,-67,-65,-64,-69,-98,-124,-112,-94,-99,]),'RETURN':([35,37,39,48,55,60,61,62,63,64,65,66,67,68,81,82,83,84,85,86,87,93,105,124,126,135,174,176,185,186,187,211,214,216,217,218,219,225,227,228,229,230,264,266,],[-119,-120,-39,-40,-125,79,-125,-125,-125,-125,-125,-125,-125,-53,-46,-47,-48,-49,-50,-51,-52,-125,-8,-125,-66,-125,-63,-68,-125,-125,-113,-54,-123,-67,-65,-64,-69,-98,79,-114,-53,-112,-94,-99,]),'LLAVEDER':([35,37,39,48,55,56,60,61,62,63,64,65,66,67,68,78,79,80,81,82,83,84,85,86,87,93,105,106,107,108,109,112,113,114,115,124,126,135,140,143,144,151,152,155,156,159,160,161,162,163,164,165,174,176,185,186,187,192,193,194,195,196,197,198,199,200,201,202,203,204,205,207,211,214,216,217,218,219,225,226,227,228,229,230,232,234,235,236,237,238,239,240,242,252,256,257,258,259,260,264,266,274,275,276,277,278,279,],[-119,-120,-39,-40,-125,75,-125,-125,-125,-125,-125,-125,-125,-125,-53,105,-125,-10,-46,-47,-48,-49,-50,-51,-52,-125,-8,-9,-11,-12,-21,-125,-125,-125,-125,-125,-66,-125,-35,-38,-34,-33,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-63,-68,-125,-125,-113,-79,-125,-125,-27,-28,-29,-30,-31,-32,-125,-125,-125,-125,-80,-90,-54,-123,-67,-65,-64,-69,-98,-125,-125,-114,-53,-112,-22,-36,-37,-86,-87,-81,-82,-125,-19,266,-103,270,-89,-18,-20,-94,-99,-125,-125,-125,-102,-100,-101,]),'CORCHIZQ':([69,109,112,113,114,115,140,143,144,151,152,155,156,159,160,161,162,163,164,165,192,193,194,195,196,197,198,199,200,201,202,203,204,205,207,212,232,234,235,236,237,238,239,240,242,244,246,258,259,260,262,271,],[90,-21,-125,-125,-125,-125,-35,-38,-34,-33,-85,-88,-84,-83,-125,208,-14,-15,-16,-17,-79,-125,-125,-27,-28,-29,-30,-31,-32,-125,-125,-125,-125,-80,-90,-125,-22,-36,-37,-86,-87,-81,-82,-125,-19,261,-59,-89,-18,-20,-125,-58,]),'PUNTO':([69,161,],[91,209,]),'IGUAL':([69,88,92,123,173,],[-125,119,-62,-61,-60,]),'INTNUM':([79,89,90,94,95,97,98,105,108,111,116,117,118,119,121,138,141,142,145,146,147,148,149,150,153,154,157,158,168,171,180,182,191,206,208,210,226,245,251,254,274,275,276,],[-125,-125,-125,-125,-125,-125,-125,-8,-93,-125,162,-91,-92,-125,-93,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,224,-93,162,162,-125,162,-125,265,224,162,162,162,]),'FLOATNUM':([79,89,90,94,95,97,98,105,108,111,116,117,118,119,121,138,141,142,145,146,147,148,149,150,153,154,157,158,168,171,180,191,206,208,210,226,245,274,275,276,],[-125,-125,-125,-125,-125,-125,-125,-8,-93,-125,163,-91,-92,-125,-93,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-93,163,163,-125,163,-125,163,163,163,]),'BOOLVAL':([79,89,90,94,95,97,98,105,108,111,116,117,118,119,121,138,141,142,145,146,147,148,149,150,153,154,157,158,168,171,180,191,206,208,210,226,245,274,275,276,],[-125,-125,-125,-125,-125,-125,-125,-8,-93,-125,164,-91,-92,-125,-93,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-125,-93,164,164,-125,164,-125,164,164,164,]),'MAS':([79,89,90,94,95,97,98,111,114,115,119,138,141,142,145,146,147,148,149,150,153,154,156,157,158,159,160,161,162,163,164,165,168,171,180,192,201,202,203,204,205,207,210,238,239,240,242,245,258,259,260,],[117,117,117,117,117,117,117,117,153,-125,117,117,117,117,117,117,117,117,117,117,117,117,-84,117,117,-83,-125,-13,-14,-15,-16,-17,117,117,117,-79,153,153,-125,-125,-80,-90,117,-81,-82,-125,-19,117,-89,-18,-20,]),'MENOS':([79,89,90,94,95,97,98,111,114,115,119,138,141,142,145,146,147,148,149,150,153,154,156,157,158,159,160,161,162,163,164,165,168,171,180,192,201,202,203,204,205,207,210,238,239,240,242,245,258,259,260,],[118,118,118,118,118,118,118,118,154,-125,118,118,118,118,118,118,118,118,118,118,118,118,-84,118,118,-83,-125,-13,-14,-15,-16,-17,118,118,118,-79,154,154,-125,-125,-80,-90,118,-81,-82,-125,-19,118,-89,-18,-20,]),'ELSE':([93,105,124,126,217,218,226,274,275,276,],[125,-8,175,-66,-65,-64,255,255,255,255,]),'IN':([105,131,226,274,275,276,],[-8,182,254,254,254,254,]),'CORCHDER':([109,112,113,114,115,119,122,140,143,144,151,152,155,156,159,160,161,162,163,164,165,192,193,194,195,196,197,198,199,200,201,202,203,204,205,207,232,234,235,236,237,238,239,240,241,242,258,259,260,],[-21,-125,-125,-125,-125,168,173,-35,-38,-34,-33,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,-125,-125,-27,-28,-29,-30,-31,-32,-125,-125,-125,-125,-80,-90,-22,-36,-37,-86,-87,-81,-82,-125,259,-19,-89,-18,-20,]),'AND':([112,113,114,115,144,151,152,155,156,159,160,161,162,163,164,165,192,193,194,195,196,197,198,199,200,201,202,203,204,205,207,236,237,238,239,240,242,258,259,260,],[141,-125,-125,-125,-34,-33,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,141,141,-27,-28,-29,-30,-31,-32,-125,-125,-125,-125,-80,-90,-86,-87,-81,-82,-125,-19,-89,-18,-20,]),'OR':([112,113,114,115,144,151,152,155,156,159,160,161,162,163,164,165,192,193,194,195,196,197,198,199,200,201,202,203,204,205,207,236,237,238,239,240,242,258,259,260,],[142,-125,-125,-125,-34,-33,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,142,142,-27,-28,-29,-30,-31,-32,-125,-125,-125,-125,-80,-90,-86,-87,-81,-82,-125,-19,-89,-18,-20,]),'MAYORQUE':([113,114,115,152,155,156,159,160,161,162,163,164,165,192,201,202,203,204,205,207,236,237,238,239,240,242,258,259,260,],[145,-125,-125,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,-125,-125,-125,-125,-80,-90,-86,-87,-81,-82,-125,-19,-89,-18,-20,]),'MENORQUE':([113,114,115,152,155,156,159,160,161,162,163,164,165,192,201,202,203,204,205,207,236,237,238,239,240,242,258,259,260,],[146,-125,-125,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,-125,-125,-125,-125,-80,-90,-86,-87,-81,-82,-125,-19,-89,-18,-20,]),'DIFERENTE':([113,114,115,152,155,156,159,160,161,162,163,164,165,192,201,202,203,204,205,207,236,237,238,239,240,242,258,259,260,],[147,-125,-125,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,-125,-125,-125,-125,-80,-90,-86,-87,-81,-82,-125,-19,-89,-18,-20,]),'MAYOROIGUAL':([113,114,115,152,155,156,159,160,161,162,163,164,165,192,201,202,203,204,205,207,236,237,238,239,240,242,258,259,260,],[148,-125,-125,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,-125,-125,-125,-125,-80,-90,-86,-87,-81,-82,-125,-19,-89,-18,-20,]),'MENOROIGUAL':([113,114,115,152,155,156,159,160,161,162,163,164,165,192,201,202,203,204,205,207,236,237,238,239,240,242,258,259,260,],[149,-125,-125,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,-125,-125,-125,-125,-80,-90,-86,-87,-81,-82,-125,-19,-89,-18,-20,]),'IGUALIGUAL':([113,114,115,152,155,156,159,160,161,162,163,164,165,192,201,202,203,204,205,207,236,237,238,239,240,242,258,259,260,],[150,-125,-125,-85,-88,-84,-83,-125,-13,-14,-15,-16,-17,-79,-125,-125,-125,-125,-80,-90,-86,-87,-81,-82,-125,-19,-89,-18,-20,]),'POR':([115,160,161,162,163,164,165,192,203,204,205,207,240,242,258,259,260,],[157,-125,-13,-14,-15,-16,-17,-79,157,157,-80,-90,-125,-19,-89,-18,-20,]),'SOBRE':([115,160,161,162,163,164,165,192,203,204,205,207,240,242,258,259,260,],[158,-125,-13,-14,-15,-16,-17,-79,158,158,-80,-90,-125,-19,-89,-18,-20,]),'READ':([119,],[169,]),'FLECHITA':([161,162,163,164,165,207,240,242,253,255,258,259,260,265,267,268,],[-13,-14,-15,-16,-17,-90,-125,-19,-125,269,-89,-18,-20,-97,272,273,]),'PUNTOSRANGO':([224,],[251,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'class':([0,],[1,]),'classparams':([3,],[4,]),'class2':([4,],[6,]),'empty':([4,5,15,24,25,30,32,49,54,55,60,61,62,63,64,65,66,67,69,76,77,79,89,90,93,94,95,97,98,111,112,113,114,115,119,120,124,128,135,138,141,142,145,146,147,148,149,150,153,154,157,158,160,168,171,180,185,186,188,190,193,194,201,202,203,204,210,212,215,220,226,227,240,245,253,262,274,275,276,],[8,11,26,33,37,43,33,43,59,68,80,68,68,68,68,68,68,68,92,101,104,108,121,121,126,121,121,121,121,121,143,151,155,159,121,172,176,181,187,191,121,121,121,121,121,121,121,121,121,121,121,121,207,121,121,121,229,37,104,172,143,143,155,155,159,159,191,246,172,181,256,80,207,121,207,246,256,256,256,]),'classparams2':([5,],[9,]),'vars':([5,15,25,135,186,],[10,25,35,186,35,]),'vars3':([5,15,24,25,32,135,186,],[12,12,34,12,34,12,12,]),'body':([6,],[14,]),'tipo':([12,54,100,103,],[18,58,136,137,]),'body2':([15,],[24,]),'vars2':([18,27,29,],[28,38,40,]),'funr':([24,32,],[31,45,]),'fun':([24,32,],[32,32,]),'multvarsdecl':([25,186,],[36,230,]),'varsr':([30,49,],[41,52,]),'bloque':([53,175,178,183,250,269,272,273,],[56,216,218,225,264,274,275,276,]),'fun2':([54,],[57,]),'estatuto':([55,61,62,63,64,65,66,67,185,],[60,81,82,83,84,85,86,87,228,]),'asignacion':([55,61,62,63,64,65,66,67,185,],[61,61,61,61,61,61,61,61,61,]),'condicion':([55,61,62,63,64,65,66,67,185,],[62,62,62,62,62,62,62,62,62,]),'escritura':([55,61,62,63,64,65,66,67,185,],[63,63,63,63,63,63,63,63,63,]),'for':([55,61,62,63,64,65,66,67,185,],[64,64,64,64,64,64,64,64,64,]),'while':([55,61,62,63,64,65,66,67,185,],[65,65,65,65,65,65,65,65,65,]),'when':([55,61,62,63,64,65,66,67,185,],[66,66,66,66,66,66,66,66,66,]),'llamada':([55,61,62,63,64,65,66,67,185,],[67,67,67,67,67,67,67,67,67,]),'bloque2':([60,227,],[78,257,]),'asignacion3':([69,],[88,]),'condicion2':([70,177,],[93,217,]),'fun3':([76,],[99,]),'funparamr':([77,188,],[102,231,]),'bloque3':([79,],[106,]),'expresion':([79,89,90,94,95,97,98,111,119,138,168,171,180,210,245,],[107,120,122,127,129,132,133,139,167,190,212,215,129,190,262,]),'megaexp':([79,89,90,94,95,97,98,111,119,138,168,171,180,210,245,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'superexp':([79,89,90,94,95,97,98,111,119,138,141,142,168,171,180,210,245,],[112,112,112,112,112,112,112,112,112,112,193,194,112,112,112,112,112,]),'exp':([79,89,90,94,95,97,98,111,119,138,141,142,145,146,147,148,149,150,168,171,180,210,245,],[113,113,113,113,113,113,113,113,113,113,113,113,195,196,197,198,199,200,113,113,113,113,113,]),'termino':([79,89,90,94,95,97,98,111,119,138,141,142,145,146,147,148,149,150,153,154,168,171,180,210,245,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,201,202,114,114,114,114,114,]),'factor':([79,89,90,94,95,97,98,111,119,138,141,142,145,146,147,148,149,150,153,154,157,158,168,171,180,210,245,],[115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,203,204,115,115,115,115,115,]),'factor2':([79,89,90,94,95,97,98,111,119,138,141,142,145,146,147,148,149,150,153,154,157,158,168,171,180,210,245,],[116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,]),'condicionr':([93,],[124,]),'esc1':([95,180,],[128,220,]),'funbody':([99,],[134,]),'megaexpr':([112,193,194,],[140,234,235,]),'oplog':([113,],[144,]),'expr':([114,201,202,],[152,236,237,]),'terminor':([115,203,204,],[156,238,239,]),'varcte':([116,206,208,226,274,275,276,],[160,240,241,253,253,253,253,]),'asignacion2':([119,],[166,]),'expresionr':([120,190,215,],[170,233,248,]),'estatutor':([124,],[174,]),'esc2':([128,220,],[179,249,]),'opc1':([135,],[185,]),'expresion2':([138,210,],[189,243,]),'varcter':([160,240,253,],[205,258,267,]),'for2':([182,],[222,]),'range':([182,254,],[223,268,]),'opc2':([185,],[227,]),'asignacion2r':([212,262,],[244,271,]),'when2':([226,274,275,276,],[252,277,278,279,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> class","S'",1,None,None,None),
  ('resultado -> class','resultado',1,'p_resultado','1eraFase.py',138),
  ('class -> CLASS CID classparams class2 body','class',5,'p_class','1eraFase.py',144),
  ('class2 -> DOSPUNTOS ID PARIZQ vars2 PARDER','class2',5,'p_class2','1eraFase.py',152),
  ('class2 -> empty','class2',1,'p_class2','1eraFase.py',153),
  ('classparams -> PARIZQ classparams2 PARDER','classparams',3,'p_classparams','1eraFase.py',159),
  ('classparams2 -> vars','classparams2',1,'p_classparams2','1eraFase.py',165),
  ('classparams2 -> empty','classparams2',1,'p_classparams2','1eraFase.py',166),
  ('bloque -> LLAVEIZQ estatuto bloque2 LLAVEDER','bloque',4,'p_bloque','1eraFase.py',172),
  ('bloque2 -> RETURN bloque3','bloque2',2,'p_bloque2','1eraFase.py',178),
  ('bloque2 -> empty','bloque2',1,'p_bloque2','1eraFase.py',179),
  ('bloque3 -> expresion','bloque3',1,'p_bloque3','1eraFase.py',185),
  ('bloque3 -> empty','bloque3',1,'p_bloque3','1eraFase.py',186),
  ('varcte -> ID','varcte',1,'p_varcte','1eraFase.py',192),
  ('varcte -> INTNUM','varcte',1,'p_varcte','1eraFase.py',193),
  ('varcte -> FLOATNUM','varcte',1,'p_varcte','1eraFase.py',194),
  ('varcte -> BOOLVAL','varcte',1,'p_varcte','1eraFase.py',195),
  ('varcte -> STRING','varcte',1,'p_varcte','1eraFase.py',196),
  ('varcte -> ID CORCHIZQ varcte CORCHDER','varcte',4,'p_varcte','1eraFase.py',197),
  ('varcte -> ID PUNTO ID','varcte',3,'p_varcte','1eraFase.py',198),
  ('varcte -> ID PARIZQ expresion2 PARDER','varcte',4,'p_varcte','1eraFase.py',199),
  ('expresion -> megaexp','expresion',1,'p_expresion','1eraFase.py',206),
  ('expresion -> ID PARIZQ expresion2 PARDER','expresion',4,'p_expresion','1eraFase.py',207),
  ('expresionr -> COMA expresion expresionr','expresionr',3,'p_expresionr','1eraFase.py',217),
  ('expresionr -> empty','expresionr',1,'p_expresionr','1eraFase.py',218),
  ('expresion2 -> expresion expresionr','expresion2',2,'p_expresion2','1eraFase.py',224),
  ('expresion2 -> empty','expresion2',1,'p_expresion2','1eraFase.py',225),
  ('oplog -> MAYORQUE exp','oplog',2,'p_oplog','1eraFase.py',231),
  ('oplog -> MENORQUE exp','oplog',2,'p_oplog','1eraFase.py',232),
  ('oplog -> DIFERENTE exp','oplog',2,'p_oplog','1eraFase.py',233),
  ('oplog -> MAYOROIGUAL exp','oplog',2,'p_oplog','1eraFase.py',234),
  ('oplog -> MENOROIGUAL exp','oplog',2,'p_oplog','1eraFase.py',235),
  ('oplog -> IGUALIGUAL exp','oplog',2,'p_oplog','1eraFase.py',236),
  ('oplog -> empty','oplog',1,'p_oplog','1eraFase.py',237),
  ('superexp -> exp oplog','superexp',2,'p_superexp','1eraFase.py',247),
  ('megaexp -> superexp megaexpr','megaexp',2,'p_megaexp','1eraFase.py',254),
  ('megaexpr -> AND superexp megaexpr','megaexpr',3,'p_megaexpr','1eraFase.py',261),
  ('megaexpr -> OR superexp megaexpr','megaexpr',3,'p_megaexpr','1eraFase.py',262),
  ('megaexpr -> empty','megaexpr',1,'p_megaexpr','1eraFase.py',263),
  ('vars -> vars3 tipo vars2 COLON','vars',4,'p_vars','1eraFase.py',273),
  ('vars -> vars3 tipo LIST vars2 COLON','vars',5,'p_vars','1eraFase.py',274),
  ('varsr -> COMA ID varsr','varsr',3,'p_varsr','1eraFase.py',286),
  ('varsr -> empty','varsr',1,'p_varsr','1eraFase.py',287),
  ('vars2 -> ID varsr','vars2',2,'p_vars2','1eraFase.py',297),
  ('vars3 -> PRIVATE','vars3',1,'p_vars3','1eraFase.py',304),
  ('vars3 -> empty','vars3',1,'p_vars3','1eraFase.py',305),
  ('estatuto -> asignacion estatuto','estatuto',2,'p_estatuto','1eraFase.py',312),
  ('estatuto -> condicion estatuto','estatuto',2,'p_estatuto','1eraFase.py',313),
  ('estatuto -> escritura estatuto','estatuto',2,'p_estatuto','1eraFase.py',314),
  ('estatuto -> for estatuto','estatuto',2,'p_estatuto','1eraFase.py',315),
  ('estatuto -> while estatuto','estatuto',2,'p_estatuto','1eraFase.py',316),
  ('estatuto -> when estatuto','estatuto',2,'p_estatuto','1eraFase.py',317),
  ('estatuto -> llamada estatuto','estatuto',2,'p_estatuto','1eraFase.py',318),
  ('estatuto -> empty','estatuto',1,'p_estatuto','1eraFase.py',319),
  ('asignacion -> ID asignacion3 IGUAL asignacion2 COLON','asignacion',5,'p_asignacion','1eraFase.py',326),
  ('asignacion2 -> expresion','asignacion2',1,'p_asignacion2','1eraFase.py',333),
  ('asignacion2 -> CORCHDER expresion asignacion2r CORCHIZQ','asignacion2',4,'p_asignacion2','1eraFase.py',334),
  ('asignacion2 -> READ PARIZQ STRING PARDER','asignacion2',4,'p_asignacion2','1eraFase.py',335),
  ('asignacion2r -> COMA expresion asignacion2r','asignacion2r',3,'p_asignacion2r','1eraFase.py',343),
  ('asignacion2r -> empty','asignacion2r',1,'p_asignacion2r','1eraFase.py',344),
  ('asignacion3 -> CORCHIZQ expresion CORCHDER','asignacion3',3,'p_asignacion3','1eraFase.py',350),
  ('asignacion3 -> PUNTO ID','asignacion3',2,'p_asignacion3','1eraFase.py',351),
  ('asignacion3 -> empty','asignacion3',1,'p_asignacion3','1eraFase.py',352),
  ('condicion -> IF condicion2 condicionr estatutor','condicion',4,'p_condicion','1eraFase.py',358),
  ('condicion2 -> PARIZQ expresion PARDER bloque','condicion2',4,'p_condicion2','1eraFase.py',364),
  ('condicionr -> ELSE IF condicion2','condicionr',3,'p_condicionr','1eraFase.py',370),
  ('condicionr -> empty','condicionr',1,'p_condicionr','1eraFase.py',371),
  ('estatutor -> ELSE bloque','estatutor',2,'p_estatutor','1eraFase.py',377),
  ('estatutor -> empty','estatutor',1,'p_estatutor','1eraFase.py',378),
  ('escritura -> WRITE PARIZQ esc1 esc2 PARDER','escritura',5,'p_escritura','1eraFase.py',384),
  ('esc1 -> expresion','esc1',1,'p_esc1','1eraFase.py',390),
  ('esc1 -> STRING','esc1',1,'p_esc1','1eraFase.py',391),
  ('esc2 -> COMA esc1 esc2','esc2',3,'p_esc2','1eraFase.py',397),
  ('esc2 -> empty','esc2',1,'p_esc2','1eraFase.py',398),
  ('tipo -> INT','tipo',1,'p_tipo','1eraFase.py',404),
  ('tipo -> FLOAT','tipo',1,'p_tipo','1eraFase.py',405),
  ('tipo -> BOOL','tipo',1,'p_tipo','1eraFase.py',406),
  ('tipo -> STRING','tipo',1,'p_tipo','1eraFase.py',407),
  ('tipo -> CID','tipo',1,'p_tipo','1eraFase.py',408),
  ('factor -> PARIZQ expresion PARDER','factor',3,'p_factor','1eraFase.py',415),
  ('factor -> factor2 varcte varcter','factor',3,'p_factor','1eraFase.py',416),
  ('terminor -> POR factor terminor','terminor',3,'p_terminor','1eraFase.py',426),
  ('terminor -> SOBRE factor terminor','terminor',3,'p_terminor','1eraFase.py',427),
  ('terminor -> empty','terminor',1,'p_terminor','1eraFase.py',428),
  ('termino -> factor terminor','termino',2,'p_termino','1eraFase.py',438),
  ('exp -> termino expr','exp',2,'p_exp','1eraFase.py',445),
  ('expr -> MAS termino expr','expr',3,'p_expr','1eraFase.py',452),
  ('expr -> MENOS termino expr','expr',3,'p_expr','1eraFase.py',453),
  ('expr -> empty','expr',1,'p_expr','1eraFase.py',454),
  ('varcter -> COMA varcte varcter','varcter',3,'p_varcter','1eraFase.py',464),
  ('varcter -> empty','varcter',1,'p_varcter','1eraFase.py',465),
  ('factor2 -> MAS','factor2',1,'p_factor2','1eraFase.py',471),
  ('factor2 -> MENOS','factor2',1,'p_factor2','1eraFase.py',472),
  ('factor2 -> empty','factor2',1,'p_factor2','1eraFase.py',473),
  ('for -> FOR PARIZQ ID IN for2 PARDER bloque','for',7,'p_for','1eraFase.py',483),
  ('for2 -> ID','for2',1,'p_for2','1eraFase.py',489),
  ('for2 -> range','for2',1,'p_for2','1eraFase.py',490),
  ('range -> INTNUM PUNTOSRANGO INTNUM','range',3,'p_range','1eraFase.py',496),
  ('while -> WHILE PARIZQ expresion PARDER bloque','while',5,'p_while','1eraFase.py',502),
  ('when -> WHEN PARIZQ expresion PARDER LLAVEIZQ when2 LLAVEDER','when',7,'p_when','1eraFase.py',508),
  ('when2 -> varcte varcter FLECHITA bloque when2','when2',5,'p_when2','1eraFase.py',514),
  ('when2 -> IN range FLECHITA bloque when2','when2',5,'p_when2','1eraFase.py',515),
  ('when2 -> ELSE FLECHITA bloque when2','when2',4,'p_when2','1eraFase.py',516),
  ('when2 -> empty','when2',1,'p_when2','1eraFase.py',517),
  ('fun -> vars3 FUN ID PARIZQ fun2 PARDER fun3 funbody','fun',8,'p_fun','1eraFase.py',523),
  ('fun2 -> tipo ID funparamr','fun2',3,'p_fun2','1eraFase.py',532),
  ('fun2 -> empty','fun2',1,'p_fun2','1eraFase.py',533),
  ('funparamr -> COMA tipo ID funparamr','funparamr',4,'p_funparamr','1eraFase.py',543),
  ('funparamr -> empty','funparamr',1,'p_funparamr','1eraFase.py',544),
  ('fun3 -> DOSPUNTOS tipo','fun3',2,'p_fun3','1eraFase.py',554),
  ('fun3 -> empty','fun3',1,'p_fun3','1eraFase.py',555),
  ('funbody -> LLAVEIZQ opc1 opc2 bloque2 LLAVEDER','funbody',5,'p_funbody','1eraFase.py',565),
  ('opc1 -> vars multvarsdecl','opc1',2,'p_opc1','1eraFase.py',572),
  ('opc1 -> empty','opc1',1,'p_opc1','1eraFase.py',573),
  ('opc2 -> estatuto','opc2',1,'p_opc2','1eraFase.py',583),
  ('opc2 -> empty','opc2',1,'p_opc2','1eraFase.py',584),
  ('body -> LLAVEIZQ body2 funr MAIN PARIZQ PARDER bloque LLAVEDER','body',8,'p_body','1eraFase.py',591),
  ('body2 -> vars multvarsdecl','body2',2,'p_body2','1eraFase.py',598),
  ('body2 -> empty','body2',1,'p_body2','1eraFase.py',599),
  ('multvarsdecl -> vars','multvarsdecl',1,'p_multvarsdecl','1eraFase.py',609),
  ('multvarsdecl -> empty','multvarsdecl',1,'p_multvarsdecl','1eraFase.py',610),
  ('funr -> fun funr','funr',2,'p_funr','1eraFase.py',620),
  ('funr -> empty','funr',1,'p_funr','1eraFase.py',621),
  ('llamada -> ID PARIZQ expresion expresionr PARDER','llamada',5,'p_llamada','1eraFase.py',631),
  ('llamada -> empty','llamada',1,'p_llamada','1eraFase.py',632),
  ('empty -> <empty>','empty',0,'p_empty','1eraFase.py',641),
]
