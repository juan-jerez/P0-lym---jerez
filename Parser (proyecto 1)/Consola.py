import lexer as lex
import sys
import parser_ as parse

"""
función encargada de la Impresión del menu
"""
def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido al analizador sintactico (parser)")
    print("1- Ejecutar aplicación")
    print("2- Salir")
    print("*******************************************")

"""
        Menu principal 
"""
'''
tokens= lex.generarTokens("textoEjemplo.txt")
texto= ''
i= 0
while i <= len(tokens) - 2:
    #texto += '<' + token + '>,'
    texto += tokens[i]
    print(i)
    i = i + 1
    print(i)
    texto += tokens[i]
    i += 1
    print(i)
print(tokens)
'''
while True:

    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        nombreArchivo= input("ingrese el nombre del archivo de texto: ")
        tokens= lex.generarTokens(nombreArchivo)
        print(tokens)
        #result= parse.analizarTokens(tokens)
        
        #if result:
        #    print("yes")
        #else:
        #    print("no")
    
    else:
        sys.exit(0)


