import re
# EXPRESIONES REGULARES
#1.
#Escriba una expresión regular que encuentre todas las coincidencias que sigan el siguiente patrón.

s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
print(re.findall(r'\Drobot\d\W', s))


#2 
#Escriba una expresión regular para cada caso:
#todos los usuarios que sigan el siguente patron. User_mentions:9
#encuentre los numero de likes: likes: 5
#que permita encontrar el numero de retweets. number of retweets: 4

