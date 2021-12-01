#1

numero=int(input('Ingrese la cantidad de numeros a promediar: '))
promedio=0
for i in range(numero):
    notas=int(input("Ingrese el número: "))
    promedio=notas+promedio

promedioTotal=(promedio/numero)
print("El promedio de las notas es: ", promedioTotal)



#1-profesor
cantidad=int(input('Ingrese la cantidad de números a introducir: '))
lista_numeros=[]
for i in range(cantidad):
    x=int(input('Ingrese la nota {} : '.format(i+1)))
    lista_numeros.append(x)

print(lista_numeros)
sumatoria=0
for j in lista_numeros:
    sumatoria+=j

print("El promedio es: {}" .format(sumatoria/cantidad))



#2
triangulo=int(input('Ingrese la altura del triángulo rectángulo: '))
i=0
for i in range(triangulo):
    i=i+1
    print('*'*i)


#2-profesor:
triangulo=int(input('Ingrese la altura del triángulo rectángulo: '))

for i in range(1,triangulo+1):
    
    print('*'*i) 

#3

triangulo=int(input('Ingrese la altura del triángulo rectángulo: '))

for i in range(1,1+triangulo):
    print(' '*(triangulo-i)+'*'*i) 

#4
numero=int(input('Introduce un número : '))
primo=True
for i in range(2,numero):
    if numero%i==0:
        primo=False
if primo:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} NO es primo")
