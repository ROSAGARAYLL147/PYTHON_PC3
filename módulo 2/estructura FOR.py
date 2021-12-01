#1
mi_lista=['Juan','Lucas','Maria','Pedro']
for nombre in mi_lista:
    print(nombre)


#2 ENUMERATE (nos indica el índice o conjunto clave-valor), imprime indice, nombre
    #for i,nombre in inumerate(mi_lista)
    #   print(i,nombre)

mi_lista=['Juan','Lucas','Maria','Pedro','Juan']
for indice,nombre in enumerate(mi_lista):
    if nombre=='Juan':
        mi_lista[indice]='Itamar'
print(mi_lista)

#Iterando sobre stings
palabra='Hola Mundo'
for i,letra in enumerate(palabra):
    print(i,letra)

#3
#No se puede hacer una reasignación de elementos sobre los TEXTOS o STRING

textoNuevo=' '
for i in palabra:
    textoNuevo=textoNuevo+i
print(textoNuevo)

# 4

textoNuevo=' '
for i in palabra:
    textoNuevo+=i
    print(textoNuevo)
print(textoNuevo)

