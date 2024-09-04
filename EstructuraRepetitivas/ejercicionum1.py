# Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos  neutros. 

comprobar= True # Se creo la variable "comprobar" y se le asigno el valor "true" para controlar el bucle "while"

while comprobar== True: # El bucle while se ejecutará mientras n <= 0

 n = int(input("Ingrese la cantidad de datos que desea procesar: "))# Ingresa la cantidad de datos que desea procesar

 if n > 0:# Si n > 0 entonces "comprobar" es igual a "false"

     comprobar = False# Si la variable "comprobar" es igual a "False" el bucle continua con el for  


     positivos=0
     negativos=0 
     nulos= 0

     for i in range(n):
        dato= float(input("ingrese un numero natural "))

        if dato>0:
            positivos +=1

        elif dato<0:
            negativos += 1

        else:
            nulos += 1
     print("la cantidad de numeros positivos fue: ",positivos,"\nLa cantida de numeros negativos fue: ",negativos,"\nLa cantidad de numeros nulos fue :", nulos)        
 else:
    print("Ingrese un numero mayor que 0 ") 