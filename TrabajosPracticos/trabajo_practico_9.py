"""
Tu tarea es crear un programa en Python con las siguientes
características:
● Agregar productos: Permite a la usuaria o usuario
agregar productos a una lista. Cada producto debe
tener un nombre y un precio.
● Consultar productos: Muestra todos los productos en la lista junto con sus
precios.
● Eliminar productos: Elimina un producto de la lista a partir de su nombre.
● Menú interactivo: El programa debe ofrecer un menú para que el usuario o
usuaria pueda elegir qué acción realizar. Debe incluirse una opción para
salir del programa.
"""
productos = {}

def mostrar_menu():
    print("\n--- Menú de Productos ---")
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Eliminar producto")
    print("4. Salir")

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    if len(nombre) == 0:
        print("El nombre del producto no puede estar vacío.")
    
    precio = input("Ingrese su precio: ").strip()
    if len(precio) <= 0 and not precio.isdigit() or float(precio) <= 0:
        print("El precio ingresado no es válido. Debe ser un número positivo.")
    
    productos[nombre.capitalize()] = float(precio)
    print(f"Producto '{nombre}' agregado con éxito.")

def consultar_productos():
    if not productos:
        print("No hay productos para mostrar.")
    else:
        print("\nLista de productos:")
        for nombre, precio in productos.items():
            print(f"{nombre}: ${precio:.2f}")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().capitalize()
    if nombre in productos:
        productos.pop(nombre)
        print(f"Producto '{nombre}' eliminado con éxito.")
    else:
        print(f"El producto '{nombre}' no se encuentra en la lista.")

def mostrar_menu():
    while True:
        print("Menú de gestión de frutas:")
        print("1. Agregar una fruta")
        print("2. Consultar la lista de frutas")
        print("3. Borrar una fruta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

mostrar_menu()
