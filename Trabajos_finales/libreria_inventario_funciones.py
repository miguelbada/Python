import sqlite3
import libreria_inventario as inv
from colorama import Fore, Style, init
# Inicializa colorama
init(autoreset=True)

# Conecta o crea la base de datos
conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS producto (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               descripcion TEXT,
               cantidad INTEGER NOT NULL,
               precio REAL NOT NULL,
               categoria TEXT NOT NULL)
''')
# Guarda los cambios
conn.commit()
# Cierra la conexión
conn.close()

inv.success_message("Base de datos 'inventario.db' creada y tabla 'producto' configurada.")

def agregar_producto():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    inv.info_message("Agregar un nuevo producto al inventario:")
    nombre, descripcion, cantidad, precio, categoria = None, None, None, None, None

    while True:
        nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
        if inv.error_null(nombre, "nombre del producto"):
            continue     

        descripcion = input("Ingrese una descripción del producto (opcional): ").strip()

        cantidad = input("Ingrese la cantidad del producto: ").strip()
        if not cantidad.isdigit() or int(cantidad) <= 0:
            inv.warning_message("La cantidad ingresada no es válida. Debe ser un número entero positivo. Intentelo nuevamente.")
            continue

        precio = input("Ingrese el precio del producto: ").strip()
        if not precio.replace('.', '', 1).isdigit() or float(precio) <= 0:
            inv.warning_message("El precio ingresado no es válido. Debe ser un número positivo. Intentelo nuevamente.")
            continue

        categoria = input("Ingrese la categoría del producto: ").strip().capitalize()
        if inv.is_null(categoria):
            continue

        break

    try:
        #Inicia la transacción
        conn.execute('BEGIN TRANSACTION;')

        cursor.execute('''
        INSERT INTO producto (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, int(cantidad), float(precio), categoria))
        
        conn.commit()
        inv.success_message(f"Producto '{nombre}' agregado con éxito.")

    except sqlite3.Error as e:
        inv.warning_message(f"[ERROR] Error en la base de datos: {e}") 
        conn.rollback() # Deshace los cambios en caso de error

    except Exception as e:
        inv.warning_message(f"Error al ingresar el nombre del producto: {e}")
        conn.rollback() # Deshace los cambios en caso de error

    finally:
        conn.close()

def consultar_productos():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    inv.info_message("Consultar productos en el inventario:")
    
    try:
        conn.execute('BEGIN TRANSACTION;')
        cursor.execute('SELECT * FROM producto')
        productos = cursor.fetchall()

        if not productos:
            inv.warning_message("No hay productos en el inventario.")
            return

        print("\nLista de productos:")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                  f"Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoría: {producto[5]}")

    except sqlite3.Error as e:
        inv.warning_message(f"[ERROR] Error al consultar la base de datos: {e}")
        conn.rollback()

    finally:
        conn.close()

def actualizar_producto():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    inv.info_message("Actualizar un producto en el inventario:")
    
    while True:
        id_producto = input("Ingrese el ID del producto a actualizar: ").strip()
        if not id_producto.isdigit():
            inv.warning_message("El ID debe ser un número entero positivo.")
            continue
        try:
            cursor.execute('SELECT * FROM producto WHERE id = ?', (id_producto,))
            producto = cursor.fetchone()

            if not producto:
                inv.warning_message(f"No se encontró un producto con ID {id_producto}.")
                continue
        except sqlite3.Error as e:
            inv.warning_message(f"[ERROR] Error al consultar la base de datos: {e}")
            conn.rollback()

        except Exception as e:
            inv.warning_message(f"Error al buscar el producto: {e}")
            conn.rollback()
        
        inv.success_message(f"Producto encontrado: {producto[1]} (ID: {producto[0]})")       
        break

    nombre, descripcion, cantidad, precio, categoria = None, None, None, None, None

    while True:
        nombre = input(f"Ingrese el nuevo nombre del producto (actual: {producto[1]}): ").strip().capitalize()
        if inv.is_null(nombre):
            nombre = producto[1]  # Mantiene el nombre actual si no se ingresa uno nuevo

        descripcion = input(f"Ingrese una nueva descripción del producto (actual: {producto[2]}): ").strip()
        if inv.is_null(descripcion):
            descripcion = producto[2]  # Mantiene la descripción actual si no se ingresa una nueva

        cantidad = input(f"Ingrese la nueva cantidad del producto (actual: {producto[3]}): ").strip()
        if not cantidad.isdigit() or int(cantidad) < 0:
            inv.warning_message("La cantidad ingresada no es válida. Debe ser un número entero positivo.")
            continue
        cantidad = int(cantidad) if cantidad else producto[3]  # Mantiene la cantidad actual si no se ingresa una nueva

        precio = input(f"Ingrese el nuevo precio del producto (actual: ${producto[4]:.2f}): ").strip()
        if not precio.replace('.', '', 1).isdigit() or float(precio) <= 0:
            inv.warning_message("El precio ingresado no es válido. Debe ser un número positivo.")
            continue
        precio = float(precio) if precio else producto[4]  # Mantiene el precio actual si no se ingresa uno nuevo

        categoria = input(f"Ingrese la nueva categoría del producto (actual: {producto[5]}): ").strip().capitalize()
        if inv.is_null(categoria):
            categoria = producto[5]  # Mantiene la categoría actual si no se ingresa una nueva  
        break

    try:    
        # Inicia la transacción
        conn.execute('BEGIN TRANSACTION;')

        cursor.execute('''
        UPDATE producto
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
        ''', (nombre, descripcion, cantidad, precio, categoria, id_producto))

        conn.commit()
        inv.success_message(f"Producto con ID {id_producto} actualizado con éxito.")

    except sqlite3.Error as e:
        inv.warning_message(f"[ERROR] Error al actualizar la base de datos: {e}")
        conn.rollback()
    except Exception as e:
        inv.warning_message(f"Error al actualizar el producto: {e}")
        conn.rollback()
    finally:
        conn.close()

def buscar_producto():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    inv.info_message("Buscar un producto en el inventario:")
    
    while True:
        busqueda = input("Ingrese el nombre del producto a buscar: ").strip().capitalize()
        if inv.is_null(busqueda):
            continue

        try:
            conn.execute('BEGIN TRANSACTION;')
            cursor.execute('SELECT * FROM producto WHERE nombre = ?', (busqueda,))
            producto = cursor.fetchone()

            if not producto:
                inv.warning_message(f"No se encontró un producto con el nombre '{busqueda}'.")
                continue

            print(f"Producto encontrado: ID: {producto[0]}, Nombre: {producto[1]}, "
                  f"Descripción: {producto[2]}, Cantidad: {producto[3]}, "
                  f"Precio: ${producto[4]:.2f}, Categoría: {producto[5]}")
            break

        except sqlite3.Error as e:
            inv.warning_message(f"[ERROR] Error al consultar la base de datos: {e}")
            conn.rollback()
        except Exception as e:
            inv.warning_message(f"Error al buscar el producto: {e}")
            conn.rollback()
        
        finally:
            conn.close()

def eliminar_producto():
    

    inv.info_message("Eliminar un producto del inventario:")
    
    while True:
        id_producto = input("Ingrese el ID del producto a eliminar: ").strip()
        if not id_producto.isdigit():
            inv.warning_message("El ID debe ser un número entero positivo.")
            continue

        try:
            conn = sqlite3.connect('inventario.db')
            cursor = conn.cursor()
            conn.execute('BEGIN TRANSACTION;')
            id_producto = int(id_producto)

            cursor.execute('SELECT * FROM producto WHERE id = ?', (id_producto,))
            producto = cursor.fetchone()

            if not producto:
                inv.warning_message(f"No se encontró un producto con ID {id_producto}.")
                continue

            inv.success_message(f"Producto encontrado: {producto[1]} (ID: {producto[0]})")
            break

        except sqlite3.Error as e:
            inv.warning_message(f"[ERROR] Error al consultar la base de datos: {e}")
            conn.rollback()
        except Exception as e:
            inv.warning_message(f"Error al buscar el producto: {e}")
            conn.rollback()
        finally:
            conn.close()

    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        conn.execute('BEGIN TRANSACTION;')

        cursor.execute('DELETE FROM producto WHERE id = ?', (id_producto,))
        conn.commit()
        inv.success_message(f"Producto con ID {id_producto} eliminado con éxito.")

    except sqlite3.Error as e:
        inv.warning_message(f"[ERROR] Error al eliminar el producto de la base de datos: {e}")
        conn.rollback()
    except Exception as e:
        inv.warning_message(f"Error al eliminar el producto: {e}")
        conn.rollback()
    finally:
        conn.close()

def buscar_cantidad_maxima_productos(cantidad= 0):
    inv.info_message("Buscar productos con cantidad máxima:")
    cantidad = input("Ingrese la cantidad máxima de productos a buscar: ").strip()
    while True:
        if not cantidad.isdigit() or int(cantidad) <= 0:
            inv.warning_message("La cantidad ingresada no es válida. Debe ser un número entero positivo.")
            continue
        cantidad = int(cantidad)
        break
    
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    inv.info_message("Buscar productos con cantidad máxima:")
    
    try:
        conn.execute('BEGIN TRANSACTION;')
        cursor.execute('SELECT * FROM producto WHERE cantidad <= ?', (cantidad,))
        productos = cursor.fetchall()

        if not productos:
            inv.warning_message(f"No hay productos con cantidad menor o igual a {cantidad}.")
            return

        print("\nProductos con cantidad menor o igual a", cantidad, ":")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")

    except sqlite3.Error as e:
        inv.warning_message(f"[ERROR] Error al consultar la base de datos: {e}")
        conn.rollback()
    except Exception as e:
        inv.warning_message(f"Error al buscar productos: {e}")
        conn.rollback()
    finally:
        conn.close()

def menu_principal():
    while True:
        inv.info_message("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Consultar productos")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Eliminar producto")
        print("6. Reportar productos con cantidad máxima")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            buscar_producto()
        elif opcion == '5':
            eliminar_producto()
        elif opcion == '6':
            buscar_cantidad_maxima_productos()
        elif opcion == '7':
            inv.success_message("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            inv.warning_message("Opción no válida. Por favor, intente de nuevo.")

