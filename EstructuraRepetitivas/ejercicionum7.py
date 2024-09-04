""" La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad  de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo  dígito de la placa de cada carro, se puede determinar el color de la calcomanía  utilizando la siguiente relación:  

DIGITO  COLOR
________________
1 O 2   Amarilla   
3 O 4   Rosa
5 O 6   Roja
7 O 8   Verde
9 O 9   Azul """

# Variables en las que se van almacenar el numero de veces que se repite cada categoria
amarillo=0
rosa=0 
roja= 0
verde=0
azul=0 

# Ingresa el numero de autos 
n= int(input("Ingrese el numero de autos "))

# Variable  que almacena la variable n
ingNumAutos= n

# Repite n veces que va ingresar el ultimo digito de la placa
for _ in range(ingNumAutos):
    while True: # bucle infinito
        try: #Comienza un bloque try para capturar excepciones que podrían ocurrir durante la conversión del tipo de dato o entrada del usuario.
            placa = int(input("Ingrese el ultimo numero de placa (entre 0 y 9): "))
            if 0<= placa <= 9:
                break # si se cumple la condicion if se interrumpe el bucle y continua con las siguientes condiciones
            else: # muestar el mesaje en el print si no se ingres un numero entre 0 y 9
                print("El ultimo numero de la placa debe estar entre 0 y 9. Ingrese de nuevo el ultimo digito de la placa. ")
        except ValueError: # Captura la excepción ValueError que ocurre si el usuario ingresa algo que no es un número entero
            print("La placa no es valida.")

    if 1<=placa<=2:# si el numero de la placa esta entre 1 y 2 le suma 1 a la variable amarillo
        amarillo +=1

    elif 3<=placa<=4: # si el numero de la placa esta entre 3 y 4 le suma 1 a la variable rosa
        rosa += 1

    elif 5<=placa<=6:
        roja += 1

    elif 7<=placa<=8:
        verde += 1
    else:
        azul += 1

# Muestra los resultados acumulados en las variables
print("La cantidad de autos con calcomania Amarilla es : ",amarillo,"\nLa cantida de autos con calcomania Rosa es : ",rosa,"\nLa cantida de autos con calcomania Roja es : ",roja, "\nLa cantida de autos con calcomania Verde es : ",verde,"\nLa cantida de autos con calcomania azul es : ",azul)        
