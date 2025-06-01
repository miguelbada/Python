"""
 1. Solicite al usuario o usuaria los nombres de los clientes y clientas uno por uno y
valide que cada nombre no esté vacío. Si se deja el campo vacío, mostrale un
mensaje de advertencia y volvé a pedir el nombre.

2. Guarde cada nombre válido en una lista, asegurándote de agregarlo con el
método .append().

3. Permití que la persona finalice la carga de nombres escribiendo la palabra "fin".
4. Una vez finalizada la carga, ordená alfabéticamente los nombres en la lista y
mostrá la lista ordenada de nombres utilizando un bucle for. 
"""
nombres = []
finalizacion = "fin"

while True:
    nombre = input('Ingrese el nombre del cliente o "fin" para terminar: ').strip()
    if nombre.lower() == finalizacion:
        break
    elif len(nombre) == 0:
        print("El nombre no puede estar vacío. Por favor, intente nuevamente.")
    else:
        nombres.append(nombre.capitalize())
# Se ordena la lista de nombres alfabéticamente.
nombres.sort()

for nombre in nombres:
    print(nombre)
    