# Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.

# Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor a 18 años.

# Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados
# no cumple los requisitos, sólo mostrar el texto “ERROR!”.


error = '"Error!"'
# La función strip() elimina los espacios iniciales y finales.
nombre = input("Ingrese su nombre:").strip()
if len(nombre) == 0:
    nombre = error

apellido = input("Ingrese su apellido:").strip()
if len(apellido) == 0:
    apellido = error

edad = int(input("Ingrese su edad:").strip())
if edad < 18:
    edad = error
else:
    edad = str(edad)

email = input("Ingrese su email:").strip()
if len(email) == 0:
    email = error

print("Nombre: "+ nombre +"\n" + "Apellido: " + apellido + "\n" + "Edad: " + edad + "\n" + "email: " + email )
