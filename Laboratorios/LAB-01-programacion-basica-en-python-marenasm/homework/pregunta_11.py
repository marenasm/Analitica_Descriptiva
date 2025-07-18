"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sum_dict = {} 
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    for line in lines:
       columns = line.strip().split("\t")
       col2_value = int(columns[1])
       col4_values = columns[3].split(",")

       for col4_value in col4_values:
           col4_value = col4_value.strip().lower()
           if col4_value not in sum_dict:
               sum_dict[col4_value] = 0
           sum_dict[col4_value] += col2_value

    return dict(sorted(sum_dict.items()))