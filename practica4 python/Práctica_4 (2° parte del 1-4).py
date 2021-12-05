import re
import path

# EXPRESIONES REGULARES
#1.
#Escriba una expresión regular que encuentre todas las coincidencias que sigan el siguiente patrón.

s = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'
print(re.findall(r'\Drobot\d\W', s))


#2 
s = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

x=re.findall(r'User_mentions\W\d',s)
y=re.findall(r'likes\W\s\d',s)
z=re.findall(r'number of retweets\W\s\d',s)
print(x)
print(y)
print(z)



#3



datos="AIshadowhunters.txt aaaaand back to my literature review. At least i have a friendly cup of coffee to keep me company",
"ouMYTAXES.txt I am worried that I won't get my $900 even though I paid tax last year"

analisis_sentimientos = datos.read_pandas(path,780,782)
regex = r"[^[2|3][A-u]]+\.txt" , analisis_sentimientos] # complete aqui
for tweet in analisis_sentimientos:
    print(tweet)
    
    #Encuentre todos los casos
    print(re.findall(regex, tweet))


#4

regex = r"[[0-9a-zA-Z\W.!#%&*$.]+@\.com$",emails]

emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

for example in emails:
    # Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
        print("The email {email_example} is a valid email".format(email_example=example))
    else:
        print("The email {email_example} is invalid".format(email_example=example))   