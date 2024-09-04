#Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.  Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja  de todo el grupo.  

# Solicita ingresar el número de veces que va a calificar
numCalifica = int(input("Ingresa el número de calificaciones: "))

# Crea una lista vacía que almacena las calificaciones
calificaciones = []

# Pide al usuario que ingrese una calificacion el # de veces que ingrese en numCalifica
for i in range(numCalifica):
    calificacion = float(input(f"Ingresa la calificación {i+1}: "))
    calificaciones.append(calificacion) #Agrega cada calificacion a la lista: calificaciones

# Calcula el promedio
promedio = sum(calificaciones) / len(calificaciones)

# Calcula la calificación más alta y más baja
calificacionMax = max(calificaciones)
calificacionMin= min(calificaciones)

# Muesta los resultados
print(f"Promedio de calificaciones: {round(promedio)}")
print(f"Calificación más alta: {calificacionMax:.1f}")
print(f"Calificación más baja: {calificacionMin:.1f}")