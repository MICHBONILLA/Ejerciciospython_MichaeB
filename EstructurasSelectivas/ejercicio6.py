#Muestra un mensaje solicitando al usuario que ingrese el número de notas.
notas = int(input("¿Cuántas notas desea ingresar? "))
#Crea una lista vacía que se utilizará para almacenar las notas ingresadas por el usuario.
canNotas = []
#For i in range(notas):Inicia un bucle que se repetirá notas veces. El valor de i tomará los valores de 0 a notas-1.
for i in range(notas):
  """Dentro del bucle,se solicita al usuario que ingrese una nota. La entrada se convierte a un número flotante utilizando float(), para permitir la entrada de notas decimales."""
  num = float(input(f"Ingrese el número {i+1}: "))
    #Agrega el número ingresado a la lista canNotas
  canNotas.append(num)
  """suma: Calcula la suma de todos los elementos en la lista canNotas utilizando la función sum(). Esta función devuelve la suma total de los elementos de la lista."""
suma= sum(canNotas)
"""Calcula el promedio de las notas dividiendo la suma total por la cantidad de notas. Usa la función round() para redondear el resultado al número entero más cercano"""
promedio = round(suma/ notas)
#Imprime el siguiente mensaje en pantalla
print(f"el promedio es de: {promedio} ")