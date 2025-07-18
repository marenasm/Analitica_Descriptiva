"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    sum = 0
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            sum += int(columns[1])
    return sum
            
