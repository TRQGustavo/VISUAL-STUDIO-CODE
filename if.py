# calcular el puntaje de credito
# se debe calcular que tanto credito tiene una persona
# en cierta cantidad finaciera, debera considerar
# cantidad de ingresos, nivel educacional y nacionalidad
# cantidad de ingresos:
# 500.000 a 1.000.000 : 300.000
# 1.000.000 a 1.500.000 : 650.000
# 1.500.000 o mas : 1.000.000
# Nivel educacional:
# Basico : x1, Medio : x1.3, Superior : x1.5
# Nacionalidad
# Chilena : +300.000, Extranjero: +0

print("Calculadora de Puntaje de Crédito")

# Solicitar datos al usuario
ingresos = int(input("Ingrese su cantidad de ingresos mensuales: "))
nivel = input("Ingrese su nivel educacional (basico, medio, superior): ")
nacionalidad = input("Ingrese su nacionalidad (chilena o extranjero): ")
puntaje=0

# Calcular puntaje base según ingresos
if ingresos >= 500000 and ingresos <= 1000000:
    puntaje = puntaje + 300000
    print("Puntaje base por ingresos: 300000")
elif ingresos > 1000000 and ingresos <= 1500000:
    puntaje = puntaje + 650000
    print("Puntaje base por ingresos: 650000")
elif ingresos > 1500000:
    puntaje = puntaje + 1000000
    print("Puntaje base por ingresos: 1000000")
else:
    print("Ingresos insuficientes para obtener puntaje")

# Ajustar por nivel educacional
if nivel == "basico":
    puntaje = puntaje * 1
    print("Multiplicador por educación: x1")
elif nivel == "medio":
    puntaje = puntaje * 1.3
    print("Multiplicador por educación: x1.3")
elif nivel == "superior":
    puntaje = puntaje * 1.5
    print("Multiplicador por educación: x1.5")
else:
    print("Nivel educacional no reconocido. No se aplica multiplicador.")

# Ajustar por nacionalidad
if nacionalidad == "chilena":
    puntaje = puntaje + 300000
    print("Bonificación por nacionalidad chilena: +300000")
elif nacionalidad == "extranjero":
    print("Sin bonificación por nacionalidad")
else:
    print("Nacionalidad no reconocida. No se aplica bonificación.")

# Resultado final
print("Puntaje de crédito final:", int(puntaje))
