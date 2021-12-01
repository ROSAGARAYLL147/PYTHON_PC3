#otro ejemplo

#3 Colocar funciones y/o clases
def isPrimo(numero):
    primo= True
    for i in range (2,numero):
        if numero%i==0:
            primo=False
            break
    return primo



#4 Mi programa
#Primero va al programa luego al paso 3 
listado_numeros= [*range(1,200)]
#para cada número evalúo si es primo o no lo es, por eso primero se le llama a la función y luego se evalúa
for numero in listado_numeros:
    if isPrimo(numero):
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} NO es primo")