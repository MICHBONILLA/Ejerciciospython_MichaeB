#Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo: (1*2*3*4*5…).


# Se crea la variable produ en 1 ya que el uno es el elemento neutro de la multiplicación
produ = 1

# Se crear una variable para construir la cadena de multiplicación que estara vacia hasta que se le ingresen los datos
cadena_multip = ""

ingreNum= int(input("Ingrese hasta que cantidad se va mutiplicar "))

# Bucle para multiplicar hasta el numero ingresado en ingreNum
for i in range(1,ingreNum+1):  # El rango en que itera va desde 1 al numero indicado en la variable ingreNum y a esta se le suma 1 para que pantalla no salga un numero menos mutiplicando
    if i == 1:
        cadena_multip += f"{i}"  # si i = 1 se agrega el 1 directamente a la cadena vacia
    else:
        cadena_multip += f" * {i}"  # si i! = 1 se añade el siguiente número junto con un "*" el cual representa la multiplicacion

    produ *= i  # Actualiza la variable produ mutiplicadolo i

# Muestra en pantalla la cadena de multiplicación junto el resultado 
print(f"{cadena_multip} = {produ}")