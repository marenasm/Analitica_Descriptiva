"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sum_dict = {}
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    for line in lines:
        columns = line.strip().split("\t")
        key = columns[0]
        col5_values = columns[4].split(",")
        
        for pair in col5_values:
            if pair:
                _, value = pair.split(":")
                value = int(value)
                if key in sum_dict:
                    sum_dict[key] += value
                else:
                    sum_dict[key] = value

    return dict(sorted(sum_dict.items()))
        