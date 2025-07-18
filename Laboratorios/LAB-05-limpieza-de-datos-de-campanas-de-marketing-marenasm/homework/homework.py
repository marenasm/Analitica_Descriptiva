"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel


def clean_campaign_data():
    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """
    import os
    import glob
    import zipfile
    import pandas as pd
    from datetime import datetime

    output_dir = "files/output"
    os.makedirs(output_dir, exist_ok=True)

    input_dir = "files/input"
    input_files = glob.glob(os.path.join(input_dir, "*.csv.zip"))

    data_frames = []
    for zip_path in input_files:
        with zipfile.ZipFile(zip_path, "r") as zip_open:
            for filename in zip_open.namelist():
                if filename.endswith(".csv"):
                    with zip_open.open(filename) as file_open:
                        df = pd.read_csv(file_open, sep=",")
                        data_frames.append(df)
    if not data_frames:
        print("No se encontraron archivos CSV en los ZIPs.")
        return

    data = pd.concat(data_frames, ignore_index=True)

    # CLIENT
    client = data[["client_id", "age", "job", "marital", "education", "credit_default", "mortgage"]].copy()
    client["job"] = client["job"].str.replace(".", "", regex=False).str.replace("-", "_", regex=False)
    client["education"] = client["education"].replace("unknown", pd.NA).str.replace(".", "_", regex=False)
    client["credit_default"] = (client["credit_default"].str.lower() == "yes").astype(int)
    client["mortgage"] = (client["mortgage"].str.lower() == "yes").astype(int)
    client.to_csv(os.path.join(output_dir, "client.csv"), index=False)

    # CAMPAIGN
    campaign = data[["client_id", "number_contacts", "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome", "month", "day"]].copy()
    campaign["previous_outcome"] = (campaign["previous_outcome"].str.lower() == "success").astype(int)
    campaign["campaign_outcome"] = (campaign["campaign_outcome"].str.lower() == "yes").astype(int)
    day = data["day"].astype(str).str.zfill(2)
    month = campaign["month"].apply(lambda x: datetime.strptime(x, "%b").strftime("%m")).str.lower()
    #month_map = {
    #    "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
    #    "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12"
    #}
    #month = data["month"].str.lower().map(month_map)
    campaign["last_contact_date"] = "2022-" + month + "-" + day
    campaign = campaign.drop(columns=["month", "day"])
    campaign.to_csv(os.path.join(output_dir, "campaign.csv"), index=False)

    # ECONOMICS
    economics = data[["client_id", "cons_price_idx", "euribor_three_months"]].copy()
    economics.to_csv(os.path.join(output_dir, "economics.csv"), index=False)

    return



if __name__ == "__main__":
    clean_campaign_data()
