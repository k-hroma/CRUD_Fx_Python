inventario = {}


def mostrar_inventario():
    if inventario:
        print(inventario)
    else:
        print("Inventario vacio")


def agregar_producto():
    global inventario
    print("Ingrese los datos del producto: ")
    id = int(input("ID: "))
    if id in inventario:
        print("El id ingresado ya existe")
        return
    nombre = input("Nombre: ").lower()
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    inventario[id] = {"Nombre": nombre, "Precio": precio, "cantidad": cantidad}
    print("Producto ingresado.")


def buscar_producto():
    id_buscar = int(input("Ingrese el ID del producto que busca: "))
    for clave, valor in inventario.items():
        id = clave
        datos = valor
    if id == id_buscar:
        print(f"Producto encontrado {datos}")
        return
    else:
        print("Producto no encontrado.")


while True:
    print("\n***Sistema de Inventario***\n")
    print("---Menú de opciones---\n\n1.Mostrar inventario\n2.Agregar nuevo producto\n3.Buscar producto por Id\n4.Salir")
    opcion = int(input("\nIngrese una opción: "))
    if opcion == 1:
        mostrar_inventario()
    elif opcion == 2:
        agregar_producto()
    elif opcion == 3:
        buscar_producto()
    elif opcion == 4:
        print("Usted ha salido del sistema.")
        break
    else:
        print("Seleccione una opción correcta: ")
