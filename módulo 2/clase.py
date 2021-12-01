#Convertir lista a conjunto , con set
lista=[1,2,5,48,1,5,5,8,8,9,7]
conjunto=set(lista)
print(conjunto)
#convertir conjunto a lista, con list
lista2=list(conjunto)
print(lista2)


triangulo=int(input('Ingrese la altura del triángulo rectángulo: '))

for i in range(triangulo):
    i=i+1
    print('*'*i)
    
triangulo=int(input('Ingrese la altura del triángulo rectángulo: '))

for i in range(1,1+triangulo):
    print(' '*(triangulo-i)+'*'*i) 
