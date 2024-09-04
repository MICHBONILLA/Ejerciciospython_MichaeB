
#Muestra un mensaje al usuario solicitando que ingrese el total de zapatillas vendidas.
ingTotZap = int(input(" ingrese el total de zapatillas vendidas "))
# Muestra un mensaje al usuario solicitando que ingrese el valor de cada zapatilla.
#Variable que almacena el valor total de las zapatillas vendidas
valorZap= int(input(" ingrese el valor de las zapatillas ")) 
#Calcula el valor total de las zapatillas vendidas multiplicando el valor de cada zapatilla por la cantidad vendida.
valoTotVend = valorZap* ingTotZap
#Inicia una condición que verifica si el total de zapatillas vendidas es mayor o igual a 3.
if ingTotZap >= 3:
   #Calcula el 20% del valor total de las zapatillas como descuento.
   desc = int(valoTotVend * 0.20)
   # Muestra el mensaje en pantalla.
   print(" Usted realizo una compra por un valor de",valoTotVend," por lo cual tiene un descuento del 20 % =",desc,"y su valor total menos el desuento es de :",valoTotVend - desc )
#Ejecuta el bloque de código siguiente si la condición del if no se cumple 
else:   
  desc = int(valoTotVend * 0.10)
  print(" Usted realizo una compra por un valor de",valoTotVend," por lo cual tiene un descuento del 10 % =",desc, "y su valor total menos el desuento es de :",valoTotVend - desc )
