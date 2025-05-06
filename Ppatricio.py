
from random import randint
aleatorio = randint(1,10)
print(f"el numero aleatorio es : {aleatorio}")
pagar =0
print("Productos")
print("1.- Chocolate $9710")
print("2.- Torta $21370")
print("3.- Pie de lim $15000")
opc = int(input(": "))
if opc ==1:
    pagar = 9710
if opc ==2:
    pagar = 21370
if opc ==3:
    pagar = 15000
descuento =0
if aleatorio ==1 or aleatorio ==2:
    descuento = 0.1
if aleatorio ==3 or aleatorio ==4:
    descuento = 0.2
if aleatorio ==5 or aleatorio ==6:
    descuento = 0.25
if aleatorio >=7:
    descuento = 0.5
# formula de descuento
print(f"se le aplica el descuento del {descuento*100}%")
print(f"valor a pagar sin descuento ${pagar}")
pagar = pagar+(1-descuento) 
print(f"valor a pagar con descuentos ${pagar}")

