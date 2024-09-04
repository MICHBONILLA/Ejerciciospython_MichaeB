"""opcion1 y opcion2: Definen las dos opciones para la marca de llanta. opcion1 es "todo terreno" y opcion2 es "otra marca"."""

opcion1 = "todo terreno"
opcion2 = "otra marca"

#Solicita al usuario que ingrese la cantidad de llantas.
numLlantas= int(input("Ingrese la cantidad de llantas a comprar "))
#Solicita al usuario que ingrese la marca de la llanta.
marcaLlanta= str(input("Ingrese la marca de la llanta (Todo terreno/Otra marca): ")).strip().lower()
    
 #Verifica si la marca ingresada no es igual a opcion1 ("todo terreno").
if marcaLlanta != opcion1:
    # Se muestra el siguiente mesaje en pantalla
    print(f"Usted no tiene descuento por llanta comprada")

    """Esta parte del código se ejecuta si la marca de la llanta es igual a opcion1 ("todo terreno"), lo que indica que el cliente puede tener derecho a descuentos."""

else:
    # Si el numero de llantas es menor a 5 cada llanta comprada tendra un valor de 300000 
    if numLlantas < 5 :
         precioLlantas= 300000
         # Se imprime el siguiente mensaje en pantalla
         print(f"Usted tiene que pagar un valor por cada llanta de:{precioLlantas}")

    # Si el numero de llantas es menor o igual 10 cada llanta comprada tendra un valor de 250000 
    elif 5 <= numLlantas<=10:
        precioLlantas= 250000
        #Se imprime el siguiente mensaje en pantalla
        print(f"Usted tiene que pagar un valor por cada llanta de:{precioLlantas}")

    # Si el numero de llantas es mayor a 10 o no es igual a alguna de las dos codiciones anteriores, cada llanta comprada tendra un valor de 200000 
    else:  
        precioLlantas= 200000
        #Se imprime el siguiente mensaje en pantalla
        print(f"Usted tiene que pagar un valor por cada llanta de:{precioLlantas}")