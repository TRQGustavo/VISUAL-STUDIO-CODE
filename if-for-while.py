
#EXPLICACION RANDOM
'''
import random
numazar=random.randint(1,30)

print(numazar)
'''

#GENERAR UN NUMERO AL AZAR ENTRE 50

"""""
import random
numeroAadivinar=random.randit(1,50)

num=int(input("adivine el numero"))

while num!=numeroAadivinar:
    print(numeroAadivinar)
    if num>numeroAadivinar:
        print("El numero a adivinar es menor")

    else:
        print("El numero a adivinar es mayor")
    num=int(input("Adivine el numero"))
print("Le achuntaste")
"""""

#EJEMPLO DE COMUNAS

"""
arancel=200000
descuento=0
print('''
      1.- LA FLORIDA 20%
      2.-LA PINTANA 30%
      3.-PTE ALTO 25%
      4.-SAN JOAQUIN 15%
      ''')

comuna=int(input("seleccione una comuna"))

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna ==4:
    descuento=15
else:
    print("Seleccion incorrecta")

grupo=int(input("Ingrese su grupo familiar(numero entero usted incluido)"))

if grupo==1:
    descuento+=2
elif grupo<=4 and grupo>=2:
    descuento+=3
elif grupo >=5:
    descuento+=4
else:
    print("seleccion incorrecta")

print("El descuento total es ", descuento)
desc=arancel*descuento/100
total=arancel-desc
print("El total a pagar es $", total)
"""

#necesito 20 pts para abrir una puerta

"""
import random
puntos=random.randint(1,30) 
print(puntos)
if puntos>=20:
    print("logro abrir la puerta")
else:
    print("puntos insuficientes")
"""

# #hacer un ludo

# import random
# turnos=random.randint(1,6)

# hacer un ludo

"""
import random
def lanzar_dado():
    return random.randint(1, 6)
def jugar_ludo():
    jugador1 = 0
    jugador2 = 0
    while jugador1 < 30 and jugador2 < 30:
        input("Jugador 1, presiona Enter para lanzar el dado...")
        dado1 = lanzar_dado()
        print(f"Jugador 1 lanzó un {dado1}")
        jugador1 += dado1
        if jugador1 >= 30:
            print("Jugador 1 ha ganado!")
            break

        input("Jugador 2, presiona Enter para lanzar el dado...")
        dado2 = lanzar_dado()
        print(f"Jugador 2 lanzó un {dado2}")
        jugador2 += dado2
        if jugador2 >= 30:
            print("Jugador 2 ha ganado!")
            break
        print(f"Posición actual: Jugador 1: {jugador1}, Jugador 2: {jugador2}")
jugar_ludo()
"""