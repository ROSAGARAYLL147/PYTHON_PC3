
def calcular (n):
   
     for i in range (1,n):
        if n<=0:
          print("Ingrese un número positivo")

        elif n==0 or n==1:
         factorial=1
         print(factorial)
      
        else:
          factorial=n*calcular(n-1)
          print(factorial)

     return factorial 
     
n=int(input("Ingrese un numero: "))
if calcular(n):
     print("El factorial es: ", )

     