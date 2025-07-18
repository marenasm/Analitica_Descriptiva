"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re

    
    # Leer el archivo y omitir las primeras 4 líneas (encabezado)
    with open("files/input/clusters_report.txt", encoding="utf-8") as file:
        lines = file.readlines()[4:]

    registros = []
    registro_actual = ""
    for line in lines:
        # Si la línea empieza con un número, es un nuevo registro
        if re.match(r"\s*\d+", line):
            if registro_actual:
                registros.append(registro_actual)
            registro_actual = line.strip()
        else:
            registro_actual += " " + line.strip()
    if registro_actual:
        registros.append(registro_actual)

    data = []
    for reg in registros:
        # Extraer los campos usando espacios como separador
        # El formato es: cluster | cantidad | porcentaje | palabras clave
        match = re.match(
            r"(\d+)\s+(\d+)\s+([\d,\.]+\s*\%?)\s+(.+)", reg
        )
        if match:
            cluster = int(match.group(1))
            cantidad = int(match.group(2))
            porcentaje = float(match.group(3).replace(",", ".").replace("%", ""))
            palabras_clave = match.group(4)
            # Limpiar y unir palabras clave
            palabras_clave = re.sub(r"\s+", " ", palabras_clave)
            palabras_clave = palabras_clave.replace(".","")
            palabras_clave = ", ".join([w.strip() for w in palabras_clave.split(",")])
            data.append([cluster, cantidad, porcentaje, palabras_clave])

    columnas = [
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave",
    ]
    df = pd.DataFrame(data, columns=columnas)
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df