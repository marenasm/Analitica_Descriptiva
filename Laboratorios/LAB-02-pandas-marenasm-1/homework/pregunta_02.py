"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    import pandas as pd

    df = pd.read_csv('files/input/tbl0.tsv', sep='\t')

    # Contar la cantidad de columnas
    cantidad_columnas = len(df.columns)

    return cantidad_columnas
