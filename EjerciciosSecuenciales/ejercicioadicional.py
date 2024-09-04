#Se declara la variable nombre del estudiante,Se declara la variable califpro en el que se ingresara la calificacion promedio de actividades,Se declara la variable acticlas para multiplicar la calificacion promedio de actividades por el 30%, Se declara la variable califprofin en el que se ingresara la calificacion del proyecto final,  Se declara la variable califprofin en el que se ingresara la calificacion del proyecto final por el 50 %, Se declara la variable califproevpar en el que se ingresara  el promedio de las evaluaciones parciales, Se declara la variable evaparcial en el que se ingresara  el promedio de las evaluaciones parciales por el 20 %, se declara la variable notafinal en el que sumare el resultado de la 3 variables acticlas+ proyectfinal+ evaparcial y la declaro int para quitar decimales, finalmente se muestra el resultado mediante print concatenando la variable nomestud  y notafinal


# Se declara la variable nombre del estudiante
nomestud= (input (" Ingrese nombre del estudiante "))
# Se declara la variable califpro en el que se ingresara la calificacion promedio de actividades
califpro= int(input(" ingrese la calificación promedio de las actividades realizadas en clase"))
# Se declara la variable acticlas para multiplicar la calificacion promedio de actividades por el 30%
acticlas= califpro * 0.30
# Se declara la variable califprofin en el que se ingresara la calificacion del proyecto final
califprofin= int(input(" ingrese la calificación del proyecto final"))  
# Se declara la variable califprofin en el que se ingresara la calificacion del proyecto final por el 50 %
proyectfinal= califprofin * 0.50
# Se declara la variable califproevpar en el que se ingresara  el promedio de las evaluaciones parciales
califproevpar= int(input(" ingrese la calificación promedio de las evaluaciones parciales"))
# Se declara la variable evaparcial en el que se ingresara  el promedio de las evaluaciones parciales por el 20 %
evaparcial= califproevpar* 0.20
# Se declara la variable notafinal en el que sumare el resultado de la 3 variables acticlas+ proyectfinal+ evaparcial y la declaro int para quitar decimales
notafinal= int (acticlas+ proyectfinal+ evaparcial)
# se muestra el resultado mediante print concatenando la variable nomestud  y notafinal
print (" La nota final de algoritmia de estudiante ", nomestud, " es: ", notafinal)
       