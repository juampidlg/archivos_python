# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo
    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    # --- Comience aquí a desarrollar su código ---
    with open ('alturas.csv')as csvfile:
        alturas = list(csv.DictReader(csvfile))
        alturas_acum = 0
        cantidad_alturas = 0
        for i in range(len(alturas)):
            if alturas[i]['genero']== genero:
                alturas_acum += float(alturas[i]['altura'])
                cantidad_alturas += 1
    print(f"La sumatoria de alturas es: {alturas_acum}")
    print(f"La cantidad de personas del genero {genero} es: {cantidad_alturas}")
    promedio = alturas_acum / cantidad_alturas
    print(f"El promedio de alturas para el genero: {genero} es de : {promedio}")
    




if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    altura_promedio("femenino")
