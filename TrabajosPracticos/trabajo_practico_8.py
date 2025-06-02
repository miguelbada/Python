"""
● Crear un diccionario llamado productos donde las claves sean los nombres
de los productos y los valores sean sus precios.
● Permitir agregar productos y sus precios hasta que se decida finalizar.
● Mostrar el contenido del diccionario después de cada operación. 
"""

productos = {}
while True:
    producto = input("Ingrese el nombre del producto, o 'fin' para terminar: ").strip()
    if producto.lower() == "fin":
        break
    elif len(producto) == 0:
        print("El nombre del producto no puede estar vacío. Por favor, intente nuevamente.")
        continue
    
    precio = input("Ingrese su precio: ").strip()
    if len(precio) <= 0 and not precio.isdigit() or float(precio) <= 0:
        print("El precio ingresado no es válido. Debe ser un número positivo.")
        continue

    productos.setdefault(producto.capitalize(), float(precio))

    print("Contenido actual de productos:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio:.2f}")
