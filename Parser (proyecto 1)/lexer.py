

'''
***listas de categorias de tokens***
'''

blockSeparators = ['robot_r',
                    'vars',
                    'procs']

conditionals = ['if',
                'else',
                ]

then = ['then']

loop = ['while']

do= ['do']

repeatTimes= ['repeat']

oneVarCommands = ['move',
                'turn',
                'face', 
                ]

noVarCommands = ["nop"]

twoVarCommands = ['assignto',
                  'goto',
                  'put',
                  'pick',
                  'movetothe',
                  'moveindir',
                  'jumptothe',
                  'jumpindir',
                ]

notCondition = ["not"]

oneVarConditions= ['facing',
                   ]

twoVarConditions= [
             'canput',
             'canpick',
             'canmoveindir',
             'canjumpindir',
             'canmovetothe',
             'canjumptothe',
            ]

D =         ['north', 
            'east', 
            'south', 
            'west'
            ]

O =         ['front', 
            'right', 
            'left', 
            'back' 
            ]

punctuation_symbols = [':', 
                    ';', 
                    '[',
                    ']',
                    '|', 
                    ','  
                    ]

'''
***Funciones para generar los tokens***
'''

def crearSignosPuntuacion(nombreArchivo):
    file= open(nombreArchivo,'r')
    text= file.read()
    text= text.lower()
    words= []
    word= ''
    for char in text:
        if char != "" and char not in punctuation_symbols:
            word += char
        elif char in punctuation_symbols:
            word= ''
            words.append(char)
        else:
            continue


def crearPalabras(nombreArchivo):
    file= open(nombreArchivo,'r')
    text= file.read()
    text= text.lower()
    newText= text.replace("\n"," ")
    words= []
    word= ''
    for char in newText:
        if char == ' ':
            if word != '':
                words.append(word)
            word= ''
        if (char != "")and char not in punctuation_symbols:
            if char != ' ':
                word += char
        elif char in punctuation_symbols:
            if word != '':
                words.append(word)
            word= ''
            words.append(char)
        else:
            continue

    file.close
    return words

def generarTokens(nombreArchivo)->list:

    words= crearPalabras(nombreArchivo)

    tokens= []

    for word in words:
        if word in blockSeparators:
            tokens.append(word)
        elif word in O:
            tokens.append("Var")
        elif word in D:
            tokens.append("Var")
        elif word in oneVarConditions:
            tokens.append("oneVarCondition")
        elif word in twoVarConditions:
            tokens.append("twoVarCondition")
        elif word in notCondition:
            tokens.append("not")
        elif word in conditionals:
            tokens.append("conditional")
        elif word in then:
            tokens.append("then")
        elif word in loop:
            tokens.append("while")
        elif word in do:
            tokens.append("do")
        elif word in repeatTimes:
            tokens.append("repeat")
        elif word.isdigit():
            tokens.append("Var")
        elif word in oneVarCommands:
            tokens.append("OneVarCommand")
        elif word in twoVarCommands:
            tokens.append("TwoVarCommand")
        elif word in noVarCommands:
            tokens.append("NoVarCommand")    
        elif word in punctuation_symbols:
            tokens.append(word)
        else:
            tokens.append("id")
            
    return (tokens)

def separarSignosDePuntuacion(tokens):
    for token in tokens:
        for caracter in token:
            if caracter in punctuation_symbols:
                continue
