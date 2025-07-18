"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    min_max_for_key = {}
    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    for line in lines:
        columns = line.strip().split("\t")
        key_value_pairs = columns[4].split(",")
        
        for pair in key_value_pairs:
            if pair:
                key, value = pair.split(":")
                value = int(value)
                
                if key not in min_max_for_key:
                    min_max_for_key[key] = [value, value]
                else:
                    min_max_for_key[key][0] = min(min_max_for_key[key][0], value)
                    min_max_for_key[key][1] = max(min_max_for_key[key][1], value)

    result = [(key, min_max_for_key[key][0], min_max_for_key[key][1]) for key in min_max_for_key]
    
    return sorted(result)