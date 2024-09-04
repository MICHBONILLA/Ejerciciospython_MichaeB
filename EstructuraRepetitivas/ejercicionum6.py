#Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un  total de n personas. 
# Pedir el número de veces que se ingresarán datos
nv = int(input("Ingrese el número de personas: "))

# Inicializar listas para cada categoría

homPresen = 0
homAusen = 0
mujePresen=0
mujeAuse=0


# Iterar para obtener la edad y el peso de cada persona
for i in range(nv):
    sexo = input(f"Ingrese el sexo (Hombre/Mujer) {i+1}: ").strip().lower()
    ausPres = input(f"Ingrese (A para ausente/P para presente): ").strip().lower()

    if sexo=="hombre"and ausPres=="p":
        homPresen+=1
    elif sexo=="hombre"and ausPres=="a":
        homAusen+=1
    elif sexo=="mujer"and ausPres=="p":
        mujePresen+=1
    else:
        mujeAuse+=1
        

# Imprimir los resultados por categoría
print("\nResultados:")
print(f"hombres presentes: {homPresen}",f"\nhombres ausentes: {homAusen}",f"\nmujeres presentes: {mujePresen}",f"\nmujeres ausentes: {mujeAuse}" )




    







