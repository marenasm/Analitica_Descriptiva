"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


import os


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd
    import os

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")
      
    df = df.copy()
    df = df.drop(['Unnamed: 0'], axis=1).dropna().drop_duplicates()
    str_cols = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "línea_credito"]
    df[str_cols] = (df[str_cols]
                    .apply(lambda x: x.str.lower()
                                       .str.replace("_", " ", regex=False)
                                       .str.replace("-", " ", regex=False)))

    df["monto_del_credito"] = df["monto_del_credito"].str.replace("[$ ,]", "", regex=True).astype(float)

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(
        lambda x: "/".join(reversed(str(x).split("/"))) if pd.notnull(x) and len(str(x).split("/")[0]) == 4 else x
    )    

    df = df.dropna().drop_duplicates()
    output_dir = "files/output"
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, "solicitudes_de_credito.csv"), sep=";", index=False)

    return 