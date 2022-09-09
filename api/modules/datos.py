
"""
Peteciones a la API de datos abierto
"""

from api.modules.utils import *
import requests

def get_tables(departamento, numero_de_registros):
    query_params = { "departamento_nom":departamento}
    try:

        response = requests.get("https://www.datos.gov.co/resource/gt2j-8ykr.json",
                                params=query_params)
        return filtrar_datos(response.json(), numero_de_registros)
    except Exception as e:
        print(e)
        return [{
        "fecha_reporte_web": "None",
        "id_de_caso": "None",
        "fecha_de_notificaci_n":"None",
        "departamento": "None",
        "departamento_nom": "None",
        "ciudad_municipio": "None",
        "ciudad_municipio_nom": "None",
        "edad": "None",
        "unidad_medida": "None",
        "sexo": "None",
        "fuente_tipo_contagio": "None",
        "ubicacion": "None",
        "estado": "None",
        "recuperado": "None",
        "fecha_inicio_sintomas": "None",
        "fecha_diagnostico": "None",
        "fecha_recuperado": "None",
        "tipo_recuperacion": "None",
        "per_etn_": "None"
        }]
