#Permiten abstraer cierta parte del código

#1.Importar librerías, ejemplos:
#import math
#import pandas as pd
#import os
#import sys


#2 Declarar constantes
#---> Estas van en mayúsculas y no en minúsculas como las variables
PI = 3.14

#3 Colocar funciones y/o clases
def isPrimo(numero):
    #numero es primo por eso true (se le asume así por el principio)
    primo= True
    for i in range (2,numero):
        if numero%i==0:
            primo=False
            break
    return primo

#4 Mi programa
#Primero va al programa luego al paso 3 
numero=int(input('Introduce un número : '))

if isPrimo(numero):
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} NO es primo")



