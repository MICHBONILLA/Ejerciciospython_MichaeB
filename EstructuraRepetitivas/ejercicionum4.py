
import time
# Ingresa el numero con el cual desea realizar la tabla de multiplicar
numTabla= int(input("Indique el numero con el que desea mostrar la tabla de multiplicar "))

multiplicando = numTabla # Se asigna el numero ingresado a la variable multiplicando

# Imprimir la tabla de multiplicar
print(f"\nTabla de multiplicar del {multiplicando}:")
for multiplicador in range(1, 11):
    producto = multiplicando * multiplicador
    time.sleep(1)
    print(f"{multiplicando} x {multiplicador} = {producto}")
    