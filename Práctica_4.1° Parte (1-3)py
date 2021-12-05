import os

#1.Escribir una función que pida un número entero entre 1 y 10
# y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
n=int(input('Ingrese un número del 1 al 10 : '))
with open(f'tabla-{n}.txt','w') as fichero:
    for i in range(1,13):
        fichero.write('{} x {} = {} \n'.format(n,i,n*i))


#2
# Escribir una función que pida un número entero entre 1 y 10,
#lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y 
# la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.


n=int(input('Ingrese un número del 1 al 10 : '))
try:
    with open(f'./tabla-{n}.txt','r') as fichero:
        f=fichero.read()

except:
    print(f'El fichero de nombre tabla-{n}.txt no existe')

else:
    print(f)


#3
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
#  y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

n=int(input('Ingrese un número entre 1 y 10:  '))
m=int(input('Ingrese un número entre 1 y 10 para mostrar la línea del fichero:  '))

try:
    with open(f'./tabla-{n}.txt','r') as fichero:
        f=fichero.readlines()
 
except: 
    print(f'El fichero de nombre tabla-{n}.txt no existe')

else:
   
    print(f[m-1])
