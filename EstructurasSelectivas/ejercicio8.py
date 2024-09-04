"""Define una función llamada obtHemoglobina que toma la variable edadMeses.Esta variable representa la edad en meses para la cual se quiere determinar el nivel de hemoglobina."""

def obtHemoglobina(edadMeses):
    
    """Comprueba si la edad en meses es menor o igual a 1. Si es así, la función devuelve 13-26, que es el nivel de hemoglobina para este rango.Valor de hemoglobina en g/dL para cada edad."""
    if edadMeses<=1:
        return "13-26"  # Nivel hemoglobina para rango de 0-1 meses
    
        """Comprueba si la edad en meses es mayor que 1 o menor o igual a 6. Si es así, la función devuelve 10-18, que es el nivel de hemoglobina para este rango.Valor de hemoglobina en g/dL para cada edad."""
    elif 1<edadMeses<=6 :
        return "10-18"  # Nivel hemoglobina para rango de 1-6 meses
    
        """Comprueba si la edad en meses es maypr que 6 o menor o igual a 12. Si es así, la función devuelve 11-15, que es el nivel de hemoglobina para este rango.Valor de hemoglobina en g/dL para cada edad.""" 
    elif 6<edadMeses <=12:
        return "11-15" # Nivel hemoglobina para rango 7-12 de meses
    
        """Comprueba si la edad en meses es mayor que 12 o menor o igual a 60. Si es así, la función devuelve 11.5-15, que es el nivel de hemoglobina para este rango.Valor de hemoglobina en g/dL para cada edad."""
    elif 12<edadMeses <=60:
        return "11.5-15"  # Nivel hemoglobina para rango de 2 a 5 años
    
        """Comprueba si la edad en meses es mayor que 60 o menor o igual a 120. Si es así, la función devuelve 12.6-15.5, que es el nivel de hemoglobina para este rango.Valor de hemoglobina en g/dL para cada edad."""
    elif 60<edadMeses <=120:
        return "12.6-15.5" # Nivel hemoglobina para rango de 6 a 10 años
    
        """Comprueba si la edad en meses es mayor que 120 o menor o igual a 180. Si es así, la función devuelve 12.6-15.5, que es el nivel de hemoglobina para este rango.Valor de hemoglobina en g/dL para cada edad."""
    elif 120<edadMeses <=180:
        return "13-15.5"   # Nivel hemoglo para rango de 11 a 15 años
    
        """ Si la edad en meses es mayor que 120, devuelve 12-16 mujeres y 14-18 hombres, que es el nivel de hemoglobina para adultos mayores de 16 años."""
    else:
        return "12-16 en mujeres y 14-18 en hombres"  # Nivel hemoglobinam para mayores de 15 años
    
    """Define una función llamada edadConvMeses que toma dos parámetros: edad y unidad. edad es el valor de la edad y unidad especifica si la edad está en años o en meses."""
def edadConvMeses(edad, unid):
    """ Verifica si la unidad es 'años'. Si es así, convierte la edad de años a meses multiplicando por 12."""
    if unid == 'años':
        return edad * 12
    
        """Si la unidad es 'meses', simplemente devuelve la edad puesto que ya está en meses."""
    elif unid == 'meses':
        return edad
    
        """ Si la unidad no es 'años' ni 'meses', lanza una excepción ValueError con un mensaje indicando que la unidad debe ser 'años' o 'meses'."""
    else:
        raise ValueError("Unidad debe ser 'años' o 'meses'.")
    
#Define la función principal del programa
def main():
     # Solicita ingresar la edad 
     edad = int(input("Introduce la edad: "))
     # Solicita ingresar la edad en meses o años
     unid = input("Introduce la unidad (años/meses): ").strip().lower()
    
     # Convierte la edad a meses
     edadaMeses = edadConvMeses(edad, unid)
    
     # Se obtiene el nivel de hemoglobina
     hemoglo = obtHemoglobina(edadaMeses)
    
     """Imprime el resultado al usuario en un formato legible, usando una f-string para incluir las variables en el mensaje."""
    
     print(f"Para una edad de {edad} {unid}, el nivel de hemoglobina es aproximadamente {hemoglo} g/dL.")
# main(): Llama la función main para que se ejecute el programa.
main()
    
   


