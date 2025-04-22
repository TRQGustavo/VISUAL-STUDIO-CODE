print("ingrese su nombre")
nombre = input("")

print("ingrese su edad")
edad=int(input())

print("Hola ", nombre)

if edad<18:
    print("usted es menor de edad")
else:
    print("usted es mayor de edad") 

print("ingrese 3 numeros")
n1 = int(input(""))   
n2 = int(input("")) 
n3 = int(input(""))
prom=(n1+n2+n3)/3
print("el promedio es ", round(prom,2))

if prom<40:
    print("usted reprobo")
else:
    print("usted paso el ramo")


# calificar las persona segun su edad
# menor de 12 es niño
# entre 12 y 18 adolescente  
# # entre 18 y 64 adolescente 
# 65 y mas adulto mayor

edad=int(input("ingrese su edad"))

if edad<12:
    print("Es un niño")
elif edad>=12 and edad<=18:
     
    print("Es un adolescente")
else:
    print