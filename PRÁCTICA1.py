#PROBLEMA 1:

nombre=input("Ingrese su nombre: ")
print("¡Hola {}!".format(nombre))


#PROBLEMA 2:

shows=int(input("Ingrese la cantidad de shows musicales vistos en el último año: \n"))
print(f"¿El usuario ha visto más de 3 shows? {shows>=3}")



#PROBLEMA 3:
num1=float(input("Ingrese un número con decimales: "))
num2=int(input("Ingrese un número entero: "))
suma= num2+num1
print("El resultado de la suma es ", suma)


#PROBLEMA 4:
payaso=int(input("Ingrese el número de payasos vendidos: "))
muñeca=int(input("Ingrese el número de muñecas vendidas: "))
pesoTotal=payaso*112+muñeca*75

print(int(input(f"El peso total del paquete que será enviado es de {pesoTotal} g.")))



#PROBLEMA 5:
num=int(input("Ingrese un número entero: "))
sumatoria = num*(num+1)/2
print("La suma de todos los enteros desde 1 hasta", num, "es: ",sumatoria)


#PROBLEMA 6:
edad=int(input("Ingrese su edad : "))
artículos= int(input("Ingrese la cantidad de artículos comprados en la tienda: "))
print(f"¿El usuario es mayor de edad? {edad>=18}")
print(f"¿El usuario compró más de 1 artículo? {artículos>=1}")


#PROBLEMA 7:
num1=int(input("Ingrese un número : "))

num2=int(input("Ingrese un número distinto : "))
while num2==num1 :
    print("Ingrese otro número que no sea igual al primer número ingresado")
    num2=int(input("Ingrese un número distinto : "))

if num1>num2:
    print(f"El mayor de los números es {num1}")
else:
    print(f"El mayor de los números es {num2}")


#PROBLEMA 8:

print("Digitalice dos números")
num1= int(input("Primer número: "))
num2= int(input("Segundo número: "))

if num2==0:
    print("¡Error! División no válida")
else:
    print("La división es:",num1/num2)



#PROBLEMA 9:
vowel= (input("Ingrese una letra : "))


if vowel=="a" or vowel=="e" or vowel=="i"or vowel=="o"or vowel=="u":
    print("Es vocal")
elif  vowel=="A" or vowel=="E" or vowel=="I"or vowel=="O"or vowel=="U":
    print("Es vocal")
else:
    print("No se puede procesar el dato")


#PROBLEMA 10:
year=int(input("Ingrese un año: "))
if year%4==0 and  year%100!=0 or year%400==0:
    print("El año es bisiesto")
else :
    print("El año no es bisiesto")



#PROBLEMA 11:
edad=int(input("Ingrese su edad: "))

if edad<4:
    entrada=0
elif 4<=edad<18:
    entrada=5
else:
    entrada=10

print(f"El precio a cobrar es de {entrada}")



#PROBLEMA 12:
lista= ['Di', 'buen', 'día', 'a', 'papa']
lista.reverse()
print(lista)


#PROBLEMA 13:
lista=['Rojo','Verde','Blanco','Negro','Rosa','Amarillo']
lista.remove('Rojo')
lista.remove('Rosa')
lista.remove('Amarillo')

print(lista)



#PROBLEMA 14:
lista=[1,1,2,3,4,4,5,1]
n = int(input('introduce valor para separar: '))
lista=lista[:n], lista[n:]
print(lista)



#PROBLEMA 15:
lista=['rojo','verde','blanco','negro','naranja']
lista.append(lista.pop(lista.index('blanco')))
print("La lista modificada es:" ,lista)




