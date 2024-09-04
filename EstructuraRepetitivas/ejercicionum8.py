# Variables donde se acumulara las calificaciones
menorA50 = 0
entre50y69 = 0
entre70y79 = 0
mas80 = 0

# Ingresa el numero de alumnos que deseo calificar
n= int(input("Ingrese el numero de alumnos que desea calificar "))

# Variable en el que se almacenara n calificaciones y se agregara al range
numEstud= n

# Lee las calificaciones de cada estudiante
for _ in range(numEstud): # Numero de veces que se va a repetir el for
    while True:
        try:
            calificacion = int(input("Ingrese la calificación del estudiante (entre 1 y 100): "))
            if 1 <= calificacion <= 100:
                break # Sale del bucle si calificacion es valida
            else:
                print("La calificación debe estar entre 1 y 100. Ingrese calificacion de nuevo.")
        except ValueError:
            print("El número no es válido.")

    # Clasifica la calificación en el rango correspondiente
    if calificacion < 50: # calificacion igual o menor de 49
        menorA50 += 1
    elif 50 <= calificacion < 70: # calificacion entre 50 y 69
        entre50y69 += 1
    elif 70 <= calificacion < 80:  # calificacion entre 70 y 79
        entre70y79 += 1
    else:  # calificacion mayor de 80
        mas80 += 1

# Muestra los resultados
print(f"Cantidad de estudiantes con calificación menor a 50 es : {menorA50}")
print(f"Cantidad de estudiantes con calificación entre 50 y 69 es : {entre50y69}")
print(f"Cantidad de estudiantes con calificación entre 70 y 79 es : {entre70y79}")
print(f"Cantidad de estudiantes con calificación de 80 o más es : {mas80}")