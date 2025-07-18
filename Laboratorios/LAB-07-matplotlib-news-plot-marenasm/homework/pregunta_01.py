"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    # Leer el archivo CSV
    df = pd.read_csv("files/input/news.csv", index_col=0)

    # Crear gráfico
    plt.figure()

    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey"
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 3,
        "Radio": 2
    }


    # Trazar cada medio 
    for columna in df.columns:
        plt.plot(df[columna], 
                 color=colors[columna],
                 label=columna,
                 zorder=zorder[columna],
                 linewidth=linewidths[columna])
        

    # Configurar gráfico
    plt.title("How people get their news", fontsize=16)

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)

    plt.gca().axes.get_yaxis().set_visible(False)

    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col]
        )

        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) + "%",
            ha='right',
            va='center',
            color=colors[col]
        )

        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
            zorder=zorder[col]
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha='left',
            va='center',
            color=colors[col]
        )

    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center'
    ) 


    # Asegurar carpeta de salida
    os.makedirs("files/plots", exist_ok=True)

    # Guardar imagen
    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()