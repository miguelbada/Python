# Registrar los ingresos mensuales de un cliente durante 6 meses. Usá un bucle while para
# solicitar el ingreso de cada mes.Validar que los ingresos sean números positivos. 
# Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

# Calcular el total acumulado durante los 6 meses. Mostrá este resultado al final del programa.

# El programa debe mostrar el apellido, nombre y dirección de correo con el formato pedido,
# y el texto correspondiente a su rango etario.

meses = 1
importe = 0

while(meses <= 6):
    ingreso = input("Ingrese el valor del " + str(meses) +" mes " + ": ").strip()
    # La función isdigit() verifica si la cadena contiene solo dígitos.
    if ingreso.isdigit() and int(ingreso) >= 0:
        numero = int(ingreso)
        importe += numero
        meses += 1
    else:
        print("El valor ingresado no es válido.")

print(f"El ingreso total acumulado durante {meses - 1} meses es: {importe}")
