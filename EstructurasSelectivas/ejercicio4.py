"""Muestra un mensaje pidiendo al usuario que ingrese el valor de la compra. La función input() captura este valor como una cadena de texto."""
valorComp= int(input("Ingrese el valor de la compra "))
"""Estas tres líneas definen las opciones disponibles para las balotas en forma de cadenas de texto. opcion1 representa una balota roja, opcion2 una balota verde y opcion3 un color diferente."""
opcion1= "balota roja"
opcion2= "balota verde"
opcion3= "color diferente"

"""Importa el módulo random, que proporciona funciones para generar valores aleatorios, como seleccionar un elemento al azar de una lista."""

import random

#Define una función llamada escogerBalota que seleccionará aleatoriamente una de las opciones.
def escogerBalota():
    #Crea una lista llamada opciones que contiene las tres posibles balotas.
    opciones = [opcion1, opcion2, opcion3]
    # Usa random.choice() para seleccionar aleatoriamente un elemento de la lista opciones y lo asigna a la variable eleccion.
    eleccion = random.choice(opciones)
    #Devuelve la balota seleccionada aleatoriamente.
    return eleccion

#Llama a la función escogerBalota y almacena la balota seleccionada en la variable resultado.
resultado = escogerBalota()
print(f"La balota escogida es: {resultado}")

#Verifica si la balota seleccionada es opcion1 (balota roja).
if resultado == opcion1:
    #Calcula el descuento aplicable (15% del valor de la compra) y lo convierte a entero. Este valor se almacena en valorDes.
    valorDes= int(valorComp*0.15)
    # Muestar meNsaje en pantalla
    print(f"Usted tiene un descuento de 15%.El valor de su compra es de: {valorComp-valorDes} ")

#Verifica si la balota seleccionada es opcion2 (balota verde).  
elif resultado == opcion2:
    #Calcula el descuento aplicable (20% del valor de la compra) y lo convierte a entero. Este valor se almacena en valorDes.
    valorDes= int(valorComp* 0.20)
    print(f"Usted tiene un descuento de 20%.El valor de su compra es de: {valorComp-valorDes} ")

#Esta sección se ejecuta si resultado no es igual a ninguna de las opciones anteriores.
else:
    print(f"Usted no tiene ningun descuento. El valor de su compra es de: {valorComp} ")

