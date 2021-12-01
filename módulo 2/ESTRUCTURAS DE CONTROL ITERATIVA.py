#1
saludo="Buenos días"
for i in range (20):
    print(saludo )
  

#2 
#variable iniciadora
anio=2001
while anio<= 2012:
    print("Informe del año: {}". format(anio))
    anio+=1

#3 Instrucción Break

c=0
while c<=5:
    print("c vale: {}". format(c))
    if c==4:
        print("Rompemos el bucle cuando c vale", c)
        break
        #break rompe el bucle WHILE
    c+=1
print("Bucle finalizado")


#4 Instrucción continue
c=0
while c<=5:
    c+=1
    if c==3 or c==4:
        print("Continuamos con la siguiente iteración ", c)
        continue
    #Continue va a continuar con el bucle while, no pasa por el print
    print("c vale ", c)

    





