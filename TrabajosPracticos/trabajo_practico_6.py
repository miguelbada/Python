# Crear una lista con los nombres de los y las clientes que vamos a procesar. Algunos nombres 
# pueden estar en blanco, y debemos detectarlo.

# Recorrer la lista y mostrar el nombre de cada cliente o clienta, junto con su posición en la 
# lista (por ejemplo, Cliente 1, Cliente 2, etc.). 

# Si encuentras a alguien cuyo nombre sea una cadena en blanco, mostrar un mensaje de alerta 
# indicando que ese dato no es válido. 

# Para los nombres válidos, convertir cada uno a formato adecuado usando .capitalize(), 
# de modo que siempre tengan la primera letra en mayúscula y el resto en minúscula.

usuarios = ["miguel", "", "Pedro", "Maria", "Ana", "  ", "Luis", "Carlos", "LAURA", "Sofia", "Javier", "LuCia"]

for i in range(len(usuarios)):
    # La función strip() elimina los espacios iniciales y finales.
    cliente = usuarios[i].strip()
    if len(cliente) == 0:
        cliente = "Dato no válido"
    else:
        cliente = cliente.capitalize()
    print(f"{cliente} {i+1}")	# falta completar el dato no válido.
    