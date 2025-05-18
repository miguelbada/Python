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