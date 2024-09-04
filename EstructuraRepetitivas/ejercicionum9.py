# Pedir el número de veces que se ingresarán datos
nv = int(input("Ingrese el número de veces: "))

# Inicializar listas para cada categoría
hombres = []
mujeres = []


# Iterar para obtener la edad y el peso de cada persona
for i in range(nv):
    sexo = input(f"Ingrese el sexo (Hombre/Mujer) {i+1}: ").strip().lower()
    edad = int(input(f"Ingrese la edad: "))

    if sexo=="hombre":
        hombres.append(edad)

    else:
        mujeres.append(edad)
        

# Imprimir los resultados por categoría
print("\nResultados:")
print(f"Peso de los hombres: {hombres}",f"\nPeso de las mujeres: {mujeres}" )

def calcular_promedio(lista):
    return sum(lista) / len(lista) if lista else 0

promedioHommbres = calcular_promedio(hombres)
promedioMujeres = calcular_promedio(mujeres)


print(f"Promedio de peso de los hombres: {promedioHommbres:.1f}")
print(f"Promedio de peso de las mujeres: {promedioMujeres:.1f}")








