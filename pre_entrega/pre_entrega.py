seleccionado = int(input("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir\n").strip())
productos = []

while True:
    match seleccionado:
        case 1:
            while True:
                producto = input("Ingrese el nombre del producto, o 'fin' para terminar: ").strip()
                if producto.lower() == "fin":
                    seleccionado = 0
                    break
                elif len(producto) == 0:
                    print("El nombre del producto no puede estar vacío. Por favor, intente nuevamente.")
                    continue

                categoria = input("Ingrese la categoría del producto: ").strip()
                if len(categoria) == 0:
                    print("La categoría del producto no puede estar vacía. Por favor, intente nuevamente.")
                    continue

                precio = input("Ingrese su precio: ").strip()
                if len(precio) <= 0 and not precio.isdigit() or float(precio) <= 0:
                    print("El precio ingresado no es válido. Debe ser un número positivo.")
                    continue

                item = {"nombre_producto": producto.capitalize(),
                        "categoria": categoria.lower(),
                        "precio": float(precio)}
        
                productos.append(item)
                print("Contenido actual de productos:")
                for item in productos:
                    print(f"{item.get("nombre_producto")} - {item.get("categoria")} - ${item.get("precio"):.2f}")

        case 2:
            print("Mostrar productos")
            if not productos:
                print("No hay productos para mostrar.")
                seleccionado = 0
                continue
            # Ordenar los productos por nombre
            productos.sort(key=lambda x: x.get("nombre_producto")) 
            # Mostrar los productos ordenados 
            for index, producto in enumerate(productos, start=1):
                print(f"{index}. {producto.get('nombre_producto')} - {producto.get('categoria')} - ${producto.get('precio'):.2f}")

            seleccionado = 0    
            continue    

        case 3:
            busqueda = input("Ingrese el nombre del producto a buscar: ").strip()
            is_found = False
            if not busqueda:
                print("El nombre del producto no puede estar vacío.")
                continue
            elif busqueda.lower() == "fin":
                seleccionado = 0
                continue
            
            for producto in productos:
                if producto.get("nombre_producto").lower() == busqueda.lower():
                    print(f"Producto encontrado: {producto.get('nombre_producto')} - {producto.get('categoria')} - ${producto.get('precio'):.2f}")
                    is_found = True

            if not is_found:
                print(f"No se encontró el producto: {busqueda}")
                   
            seleccionado = 0
            continue     
           
        case 4:
            busqueda = input("Ingrese el nombre del producto que desea eliminar: ").strip()
            is_found = False

            if not busqueda:
                print("El nombre del producto no puede estar vacío.")
                continue
            elif busqueda.lower() == "fin":
                seleccionado = 0
                continue
            for producto in productos: 
                if producto.get("nombre_producto").lower() == busqueda.lower():
                    productos.remove(producto)
                    print(f"Producto eliminado: {producto.get('nombre_producto')}")
                    is_found = True

            if not is_found:
                print(f"No se encontró el producto: {busqueda}")

            seleccionado = 0
            continue
        case 5:
            print("Fin del programa.")
            break
        case _:
            seleccionado = int(input("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir\n").strip())
            continue
