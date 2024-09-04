# requiero ingresar las 3 variables notas con un imput y defino el tipo de dato como entero
nota1 = int(input(" ingrese la primera nota "))
nota2 = int(input(" ingrese la segunda nota "))
nota3 = int(input(" ingrese la tercera nota "))
# defino la variable promedio sumando las 3 variables  y diviendolas entre 3
promedio = (nota1+nota2+nota3)/3
# coloco la condicion si promedio es mayor o igual 70 entonces
if promedio >= 70:
 # con un print mostrara "aprueba materia " 
 print("aprueba materia")
 # si no se cumple al aterior condicion con un print " no aprueba"
else:
 print("no aprueba")