#ARGS: 
#Permite desempacar datos de una lista, tupla o biblioteca
#Hay que colocar un *(asterisco) al inicio cuando se ve un conjunto , ejemplo print(suma(*lista))
#  y también colocarlo cuando escribo args, así: *args

#Ejemplo:


def suma_independiente (*args):
    suma=0
    for arg in args:
        suma+=arg
    return suma

listado=[12,2,5,7,23]
print(suma_independiente(*listado))

#KWARGS:
#Cuando no se sabe la cantidad de valores, se da con doble asterisco **. Es más que todo para los diccionarios

def calcular(importe,descuento):
    return importe*(1-descuento/100)

datos={'importe': 1500, 'descuento':10}

print(calcular(**datos))

