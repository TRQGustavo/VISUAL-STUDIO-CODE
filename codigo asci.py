
print("Ingrese 2 digitos")

n1=int(input("ingrese un numero"))
n2=int(input("ingrese un numero"))

while n1>n2:
    print("El segundo numero puede ser menor ")
    n2=int(input("ingrese un numero"))

import random
from random import randint

numAzar=randint(n1,n2)
numAzar=random.randint(n1,n2)
print(""*numAzar)