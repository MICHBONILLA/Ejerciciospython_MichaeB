"""Una persona debe realizar un muestreo con 50 personas para determinar el  promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.  Las categorías se determinar de acuerdo a la siguiente tabla: 

CATEGORIA          EDAD
Niños              0 - 12 
Jovenes            13 - 29
Adultos            30 - 59
Ancianos           60 en adentante"""


# Solicita ingresar el número de veces que se ingresarán datos
nv = int(input("Ingrese el número de veces: "))

# Se crean listas para almacenar datos por cada categoría
pesoNiño = []
pesoJoven = []
pesoAdulto = []
pesoAnciano = []

# Itera n numero de veces para ingresar edad y peso de cada persona
for i in range(nv):
    edad = int(input(f"Ingrese la edad {i+1}: ")) 
    peso = float(input(f"Ingrese el peso: "))

    if 0 <= edad <= 12: # si edad => 0 y =>12 agregar a la categoria pesoNiño
        pesoNiño.append(peso)
        print("Categoría niños")

    elif 13 <= edad <= 29:
        pesoJoven.append(peso)
        print("Categoría jóvenes")

    elif 30 <= edad <= 59:
        pesoAdulto.append(peso)
        print("Categoría adultos")

    else:
        pesoAnciano.append(peso)
        print("Categoría ancianos")


# Muestra los resultados por de las listas por categoría
print("\nResultados:")
print(f"Pesos de niños: {pesoNiño}",f"\nPesos de jóvenes: {pesoJoven}",f"\nPesos de adultos: {pesoAdulto}",f"\nPesos de ancianos: {pesoAnciano}")


# Se define una funcion con un argumento llamado lista. 
def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else 0 # calcula los promedios en cada lista y verifica si alguna lista esta vacia para agregarle un 0 y evitar dividirla por 0 y que arroje un error 
 

# calcula los promedios
promedioNiño = calcular_promedio(pesoNiño)
promedioJoven = calcular_promedio(pesoJoven)
promedioAdulto = calcular_promedio(pesoAdulto)
promedioAnciano = calcular_promedio(pesoAnciano)

# Muestra los promedios en variables promedio y el :.1f le quita un decimal al resultado
print(f"Promedio de peso de niños: {promedioNiño:.1f}")
print(f"Promedio de peso de jóvenes: {promedioJoven:.1f}")
print(f"Promedio de peso de adultos: {promedioAdulto:.1f}")
print(f"Promedio de peso de ancianos: {promedioAnciano:.1f}")
    