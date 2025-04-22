# explicacion y uso de for

# for i in range(num):

#    print("i")


#num=9
#for i in range(10):
   #print("num,"x", i+1, "=", (i+1)*num")

cant=int(input("ingrese la el numero de notas"))
suma=0
for i in range(cant):
  print("ingrese la nota", i+1)
  nota=float(input())
  suma=suma+nota
prom=suma/cant
print("el promedio es ", round(prom))


