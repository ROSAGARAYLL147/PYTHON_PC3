#1
frase =input("Ingrese una frase: ")
palabras= frase.split(' ')
print(len(palabras[-1]))

#2

frase =input("Ingrese una frase: ")
palabras= frase.split(' ')
for i in palabras:
    print(i.capitalize(), end=" ")
print()

#3

class CIRCULO:
    def __init__(self, radio):
        self.radio= radio
        
    def print_area(self):
        print("El área del círculo es : ", self.radio*self.radio)

circulo_1= CIRCULO(5)
circulo_1.print_area()
print(circulo_1)



#4
class rectangulo:
    def __init__(self, largo, ancho):
        self.largo= largo
        self.ancho= ancho

    def print_datos(self):
        print("El largo  del rectangulo es : {}".format(self.largo))
        print("El ancho  del rectangulo es : {}".format(self.ancho))

    def print_area(self):
        print("El área es: ", self.largo*self.ancho)
        
rectangulo_1=rectangulo(5,8)
rectangulo_1.print_datos()
rectangulo_1.print_area() 
print(rectangulo_1)




#5

class Alumno:
    def __init__(self, nombre, numero_registro) -> None:
        self.nombre=nombre
        self.numero_registro=numero_registro
        
      
    def Display(self):
        print("El nombre del estudiante es : {}".format(self.nombre))
        print("El numero de registro del estudiante es : {}".format(self.numero_registro))

    def setAge(self,edad):
        return edad
        

    def setNota(self,nota):
        return nota

   
     
alumno_1=Alumno("Juan", 20)
alumno_1.Display()
age=alumno_1.setAge(15)
score=alumno_1.setNota(6)

print("El alumno tiene una edad de: {}".format(age))
print("El alumno tiene la nota: {}". format(score))
print(alumno_1)



#6

lista=input("Ingrese una lista de calificaciones separadas por comas: ")
lista=lista.split()
for i in lista:
    print(i.strip())


print(lista)


#7

def pascal(n):

    lista = [[1],[1,1]]
    for i in range(1,n):
        linea = [1]
        for j in range(0,len(lista[i])-1):
            linea.extend([ lista[i][j] + lista[i][j+1] ])
        linea += [1]
        lista.append(linea)
    return lista
 
try:
    n = int(input("Numero de lineas para triangulo de Pascal: "))
    resultado = pascal(n)
 
    for i in resultado:
        print (i)
except:
    print ("Digite otro numero")


#8

import random
lista = []
for i in range(1,21):
	lista.append(random.randint(0,100))


print(lista)



#9




#10

