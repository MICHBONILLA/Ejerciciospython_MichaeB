#Muestra un mensaje solicitando al usuario que ingrese el total de piezas.
ingNumPie = int(input(" ingrese el total de piezas"))
#Muestra un mensaje solicitando al usuario que ingrese el valor de cada pieza.
valorPie= int(input(" ingrese el valor de la pieza "))
#Calcula el monto total de la venta multiplicando el número de piezas por el valor de cada pieza.
monTototVen = ingNumPie * valorPie

#Inicia una condición para verificar si el monto total de la venta es mayor o igual a 500,000.
if monTototVen >= 500000:
  #Calcula el 55% del monto total de la venta como el valor invertido de su propio dinero.
   desc1 = int(monTototVen * 0.55) 
   #Calcula el 30% del monto total de la venta como el valor invertido de su propio dinero.
   desc2 = int(monTototVen * 0.3) 
   #Calcula el valor del crédito solicitado al fabricante restando el valor invertido de su propio dinero y el valor prestado al banco del monto total de la venta.
   valSoFab= (monTototVen-desc1-desc2)
   # Se muestra el siguiente mensaje en pantalla
   print("El valor invertido de su propio dinero es de",desc1," , el valor prestado al banco es de ",desc2," y el valor del credito solicitado al fabricante es de", valSoFab)


# Ejecuta el bloque de código siguiente si el monto total de la venta es menor que 500,000.
else: 
   #Calcula el 70% del monto total de la venta como el valor invertido de su propio dinero.
   desc1 = int(monTototVen * 0.70) 
   #Calcula el 30% del monto total de la venta como el valor invertido de su propio dinero.
   desc2 = int(monTototVen * 0.3) 
   #Calcula el 20% del monto total de la venta como el valor invertido de su propio dinero.
   intPorCre = int(desc2 *0.20)
   #Calcula el monto total que cobra el fabricante sumando los intereses al valor del crédito solicitado.
   montoTotalFab = (intPorCre+desc2)
   # Se muestra el siguiente mensaje en pantalla
   print("El valor invertido de su propio dinero es de",desc1," , el valor del credito que solicitara al fabricante es de:",desc2," y el valor del 20 porciento sobre la cantidad que se le paga a credito la fabricante es de",intPorCre," y el valor total que cobra el fabricante con intereses es de:", montoTotalFab)

