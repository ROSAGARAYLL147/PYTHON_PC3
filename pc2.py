#PROBLEMA 1:

for i in range (1500,2700):
        if i%7==0 and i%5==0:
            print(f"{i} Es divisible por 7 y es múltiplo de 5 ")




#PROBLEMA 2:

n=0
while n<5:
     n+=1
     print(" *"*n)
if(n==5):
     
   
     print((n-1)*" *")
     print((n-2)*" *")
     print((n-3)*" *")
     print((n-4)*" *")
     
#PROBLEMA 3:
list = [1,2,3,4,5,6,7,8,9]
par=0
impar=0
for i in list:
    if i %2==0:
       par+=1
    else :
        impar+=1
      
print("Cantidad de números pares: ", par)
print("Cantidad de números impares: ", impar)

#PROBLEMA 4:

lista= [1452, 11.23, 1+2j,True,'Python',(0, -1),[5, 12],{"Clase":'V',"Seccion": 'A'} ]
for i in range(len(lista)):
    print("Elemento: {} - Tipo de dato {}: ".format(lista[i], type(lista[i])))






#PROBLEMA 8:
muestra="1234abcd"
print(muestra[::-1])

#PROBLEMA 9:
lista=[1,1,5,4,7,7,10,12,9,9,1,7,84,25,55,14,10]
nuevaLista=set(lista)
print(nuevaLista)

#PROBLEMA 10:
def conocer(numeral):
    primo=True
    for i in range (2,numeral):
        if numeral %i==0:
            primo = False
            break
    return primo


numeral=int(input("Ingrese un número: "))
if conocer(numeral):
    print("El numero ", numeral, "es primo")
else:
        print("El numero ", numeral, "no es primo")








