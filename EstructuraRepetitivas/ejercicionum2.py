#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos  números.
def numerNegativ():
    numPositivos = []
    
    print("Por favor, ingresa 10 números negativos:")
    
    for i in range(10):
        while True:
            try:
                numero = int(input(f"Ingrese el número negativo {i + 1}: "))
                if numero < 0:
                    # Convertir a positivo y añadir a la lista
                    numPositivos.append(abs(numero))
                    break
                else:
                    print("El número ingresado no es negativo. Por favor, ingresa un número negativo.")
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número entero.")
    
    suma = sum(numPositivos)
    
    print(f"Los números positivos convertidos son: {numPositivos}")
    print(f"La suma de los números positivos es: {suma}")
    
# Ejecutar la función
numerNegativ()