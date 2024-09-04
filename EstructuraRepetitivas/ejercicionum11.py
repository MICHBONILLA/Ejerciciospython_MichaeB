#Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa  se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio  ,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos  que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad  sea igual a 0. 

import sys # Importo el metodo sys para para finalizar el programa cuando ingEdad = 0

nv = int(input("Ingrese el número de personas: ")) # Ingresa un numero n de personas a procesar

# Variables en las que se van almacenando datos desde 0 sobre el tipo de sexo
sexoHom = 0
sexoMuj= 0

# Listas vacias en la que se van ingresando los datos de edad y altura
edad=[]
altura=[]

# Variables en la que se van acumulando el numero de veces que se repite los datos mayores a 1.70  y menores o iguales a 1.50 
cont_mayor_170 = 0
cont_menor_igual_150 = 0

# Iterar para obtener la edad y el peso de cada persona
for i in range(nv):
    sexo = input(f"Ingrese el sexo (Hombre/Mujer) {i+1}: ").strip().lower()
    ingEdad = int(input(f"Ingrese la edad {i+1}: "))
    if ingEdad == 0:
        print("La edad ingresada es igual a 0. Programa finalizado.")
        sys.exit()
    ingAltura = float(input(f"Ingrese la altura: "))

    if sexo=="hombre":
        sexoHom+=1
        edad.append(ingEdad)
        altura.append(ingAltura)
    elif sexo=="mujer":
        sexoMuj+=1
        edad.append(ingEdad)
        altura.append(ingAltura)
    else:
        print("ingrese los datos de nuevo")

    if ingAltura > 1.70:
        cont_mayor_170 += 1
    if ingAltura <= 1.50:
        cont_menor_igual_150 += 1


print("\nResultados:")
print(f"Cantidad de hombres: {sexoHom}",f"\nCantidad de mujeres: {sexoMuj}",f"\nEdades: {edad}",f"\nAlturas: {altura}")



promedioAltura = sum(altura)/ len(altura)


print(f"Promedio de alturas: {promedioAltura:.2f}")

print(f"Cantidad de alumnos con altura mayor a 1.70 cm: {cont_mayor_170}")
print(f"Cantidad de alumnos con altura menor o igual a 1.50 cm: {cont_menor_igual_150}")
