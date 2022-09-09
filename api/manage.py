
from api.modules.datos import get_tables

def get_information(departamento, numero_de_registros):
    """
    Busca la información en la API de datos abiertos
    
    returns
        list[dict] : lista de json con los datos encontrados
    """
    return get_tables(departamento, numero_de_registros)
