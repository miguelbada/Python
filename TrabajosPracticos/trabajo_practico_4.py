# Formatee correctamente los textos ingresados en “apellido” y “nombre”, convirtiendo la primera
# letra de cada palabra a mayúsculas y el resto en minúsculas.

# Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.

# Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años,
# “Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años.)

error = '"Error!"'
rango_etario = ""
# La función strip() elimina los espacios iniciales y finales.
nombre = input("Ingrese su nombre:").strip()
if len(nombre) == 0:
    nombre = error
nombre = nombre.capitalize()

apellido = input("Ingrese su apellido:").strip()
if len(apellido) == 0:
    apellido = error
apellido = apellido.capitalize()

edad = int(input("Ingrese su edad:").strip())
if edad < 15:
    edad = error
    rango_etario = "Niño/a"
elif edad < 18:
    rango_etario = "Adolescente"
else:
    rango_etario = "Adulto/a"

email = input("Ingrese su email:").strip()
if "@" not in email or email.count("@") != 1:
    email = error

print("Nombre: "+ nombre +"\n" + "Apellido: " + apellido + "\n" + "Edad: " + str(edad) 
      + "\n" + "email: " + email + "\n" + "Rango etario: " + rango_etario)
