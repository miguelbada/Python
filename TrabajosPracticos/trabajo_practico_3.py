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
