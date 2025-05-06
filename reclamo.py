# crear un libro de reclamos simple donde tenga 5 opciones
# 1. Agregar reclamo
# 2. Ver reclamos
# 3. Buscar reclamo
# 4. Modificar reclamo
# 5. Eliminar reclamo
# 6. Salir
print("Bienvenido al libro de reclamos")
print("1. La isi me deja en visto")
print("2. La isi no me devuelve la llamda")
print("3. La isi no se preocupa por mi ")
print("4. La isi no me presta plata")
print("5. la isi no me habla en la U")
print("6. Se queja que no le respondo cuando ella no me habla")
reclamos = []
while True:
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        reclamo = input("Ingrese su reclamo: ")
        reclamos.append(reclamo)
        print("Reclamo agregado.")
    elif opcion == 2:
        if len(reclamos) == 0:
            print("No hay reclamos registrados.")
        else:
            print("Reclamos registrados:")
            for i, reclamo in enumerate(reclamos):
                print(f"{i + 1}. {reclamo}")
    elif opcion == 3:
        busqueda = input("Ingrese el reclamo a buscar: ")
        if busqueda in reclamos:
            print(f"Reclamo encontrado: {busqueda}")
        else:
            print("Reclamo no encontrado.")
    elif opcion == 4:
        busqueda = input("Ingrese el reclamo a modificar: ")
        if busqueda in reclamos:
            nuevo_reclamo = input("Ingrese el nuevo reclamo: ")
            index = reclamos.index(busqueda)
            reclamos[index] = nuevo_reclamo
            print("Reclamo modificado.")
        else:
            print("Reclamo no encontrado.")
    elif opcion == 5:
        busqueda = input("Ingrese el reclamo a eliminar: ")
        if busqueda in reclamos:
            reclamos.remove(busqueda)
            print("Reclamo eliminado.")
        else:
            print("Reclamo no encontrado.")
    elif opcion == 6:
        print("Saliendo del libro de reclamos.")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

