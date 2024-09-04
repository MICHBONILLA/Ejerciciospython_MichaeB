# se declara la variable num 1 se declara la variable num 2, se declara la variable num 3, se saca la variable promedio tomando la variable suma y diviendola entre 3 con dos // para quitar decimales y finalemente se muestra el resultado mediante f print concatenando la variable promedio


# se declara la variable num 1
num1= int(input(" indique el primer numero "))
# se declara la variable num 2
num2= int(input(" indique el segundo numero "))
# se declara la variable num 3
num3= int(input(" indique el tercer numero "))
# se suman  las tres variables
suma = (num1 + num2 + num3)
# se saca la variable promedio tomando la variable suma y diviendola entre 3 con dos // para quitar decimales
promedio = suma//3
# se muestra el resultado mediante f print concatenando la variable promedio
print (f"El promedio de los numeros ingresados es: {promedio}")