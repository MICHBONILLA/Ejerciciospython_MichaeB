# Se declara la variable nombre del vendedor, Se declara la variable sueldo, Se declara la variable comision, se declara la variable sueldtot sumando la variable sueld + comision y finalmente se muestra el resultado mediante print concatenando las variables nombvend,sueld,comision y sueldtot

# Se declara la variable nombre del vendedor
nombvend= (input (" Ingrese el nombre del vendedor "))
# Se declara la variable sueldo
sueld= int(input(" Ingrese el sueldo "))
# Se declara la variable comision
comision= int (input ( " Ingrese el valor de la comisión de las ventas realizadas "))
# se declara la variable sueldtot sumando la variable sueld + comision
sueldtot = sueld+comision
# se muestra el resultado mediante print concatenando las variables nombvend,sueld,comision y sueldtot
print(" El vendedor : ", nombvend, " tiene un sueldo de:", sueld, "durante el mes tuvo una comision de:", comision, " y su sueldo total es de:", sueldtot )