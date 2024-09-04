#Definen las cadenas que representan las dos opciones válidas para el sexo: "masculino" y "femenino".
opcion1= "masculino"
opcion2= "femenino"

"""Sex= (input("Masculino/Femenino")Asegura que la entrada del usuario sea tratada como una cadena de texto(Masculino/Femenino). """
#El.strip() Elimina cualquier espacio en blanco al principio y al final de la cadena ingresada.
"""El.lower() Convierte la cadena a minúsculas para normalizar la entrada del usuario y facilitar la comparación con las opciones definidas."""

Sex= (input("Ingrese el sexo (Masculino/Femenino):")).strip().lower()

#Verifica si el valor de Sex no es igual a opcion1 ("masculino") ni a opcion2 ("femenino").
if Sex != opcion1 and Sex != opcion2:
 
 """Si la condición es verdadera (es decir, la entrada no es ni "masculino" ni "femenino"), muestra un mensaje pidiendo al usuario que verifique la entrada."""

 print("por favor verifique que sexo esta bien escrito")

#Si la entrada de Sex es válida (es decir, es "masculino" o "femenino"), se ejecuta el bloque else.

else:

#Muestra un mensaje solicitando al usuario que ingrese su edad. La entrada del usuario se convierte a un número entero y se almacena en la variable Edad.
 Edad= int(input("ingrese la edad "))

#Verifica si el valor de Sex es igual a opcion2 ("femenino").
if Sex == opcion2:
    """Calcula el número de pulsaciones basado en la fórmula (220 - Edad) / 10 para mujeres. Usa la función round() para redondear el resultado al número entero más cercano."""
    numPul= round((220- Edad)/ 10)
    #Muestra el siguiente mensaje en pantalla
    print(f"Su numero de pulsaciones es de :{numPul}")

#Esta parte del código se ejecuta si Sex no es igual a opcion2. En otras palabras, se asume que Sex es "masculino".
else:
    #Calcula el número de pulsaciones basado en la fórmula (210 - Edad) / 10 para hombres. Usa round() para redondear el resultado al número entero más cercano.
    numPul= round((210- Edad)/ 10)
    #Muestra el siguiente mensaje en pantalla
    print(f"Su numero de pulsaciones es de :{numPul}")

