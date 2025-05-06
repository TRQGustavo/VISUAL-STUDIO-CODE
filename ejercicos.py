cant=int(input("cuantos productor llevara"))
for i in range(cant):
    print('''
    Que prducto llevara?
    1.- diazepam $9000
    2.- Metametazona $18500
    3.- Oblea China $1000 ''')
    op=int(input())
    if op==1:
        print("Usted llevara diazepam")
        total=total+9000
    elif op==2:
        print("Usted llevara metametazona")
        total=total=18500
    elif op==3:
        print("Usted llevara oblea china")
        total=total=1000
    else:
        print("opcion no valida")
print("El total neto es", total)
print("El total mas IVA es", total*1.19)


cant=int(input("num de votantes"))
for i in range (cant):
        print('''
        Votantes a elegir
        1.- Kayzer
        2.- Nose 
        3.- Rayth ''')
        op=int(input)
        
        


