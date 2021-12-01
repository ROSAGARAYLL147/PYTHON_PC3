#Es posible colocar valores por defecto en nuestras funciones, así si no se pasa ninguín parámetro, nuestra función seguirá funcionando.

#1
def bar(x=2):
    return x+90

print(bar())

#EJEMPLOS
#Realiza una función que indique si un número pasado por parámetro es par o impar.

def parOimpar(numero):
    if numero%2==0:
        return numero


numero=int(input('Ingrese un numero: '))
if parOimpar(numero) :
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')


#EJEMPLOS
#Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del rectangulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura

def area_rectangulo(base,altura):
    return base*altura

b=int(input('Ingrese la base para el rectángulo: '))
h= int(input('Ingrese la altura para el rectángulo: '))

print('El área del rectángulo es :',area_rectangulo(b,h))





