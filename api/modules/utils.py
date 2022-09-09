"""
Funciones utiles
"""
def filtrar_datos(list_data: list[dict], numero_de_registros):
    new_list_data = []
    if len(list_data) < numero_de_registros: 
        new_list_data = [list_data[i]
                        for i in range(0,len(list_data))]
    else:
        new_list_data = [list_data[i]
                        for i in range(0,numero_de_registros)]
    return new_list_data