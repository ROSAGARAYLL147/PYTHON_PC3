
lista=input("Ingrese una lista de calificaciones separadas por comas: ")
lista=lista.split()
for i in lista:
    print(i.strip())

lista=lista.split(",")
for i in lista:
    print(i.strip())
print(lista)
