"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import numpy as np


def clean_data():
  

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.replace(r'^\s*$', np.NaN, regex=True)
    df.dropna(inplace=True)

    del df ["Unnamed: 0"]

    df.astype({'sexo':'string','tipo_de_emprendimiento':'string','idea_negocio':'string','barrio':'string','línea_credito':'string'})
    df['sexo'] = df['sexo'].apply(str.lower)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].astype(str)
    df['barrio'] = df['barrio'].astype(str)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(str.lower)
    df['idea_negocio'] = df['idea_negocio'].apply(str.lower)
    df['barrio'] = df['barrio'].apply(str.lower)
    df['línea_credito'] = df['línea_credito'].apply(str.lower)


    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: x.replace('$', '').replace(',', '')
                                    if isinstance(x, str) else x).astype(float)
    df.idea_negocio = df.idea_negocio.str.replace("_", " ", regex=False)
    df.idea_negocio = df.idea_negocio.str.replace("-", " ", regex=False)
    df.idea_negocio = df.idea_negocio.str.replace(".", " ", regex=False)
    df.idea_negocio = df.idea_negocio.str.replace("  ", " ", regex=False)
    df.idea_negocio = df['idea_negocio'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    df.barrio = df.barrio.str.replace("_", " ", regex=False)
    df.barrio = df.barrio.str.replace("-", " ", regex=False)
    df.barrio = df.barrio.str.replace(".", " ", regex=False)
    df.barrio = df['barrio'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    df.línea_credito = df.línea_credito.str.replace("_", " ", regex=False)
    df.línea_credito = df.línea_credito.str.replace("-", " ", regex=False)
    df.línea_credito = df.línea_credito.str.replace(".", " ", regex=False)
    df.línea_credito = df.línea_credito.str.replace("  ", " ", regex=False)
    df.línea_credito = df['línea_credito'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df
