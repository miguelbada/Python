usuarios = ["miguel", "", "Pedro", "Maria", "Ana", "  ", "Luis", "Carlos", "LAURA", "Sofia", "Javier", "LuCia"]

for i in range(len(usuarios)):
    # La función strip() elimina los espacios iniciales y finales.
    cliente = usuarios[i].strip()
    if len(cliente) == 0:
        cliente = "Dato no válido"
    else:
        cliente = cliente.capitalize()

    print(f"{cliente} {i+1}")	