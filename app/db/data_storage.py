
from flask import current_app

class DataStorage:
    """
        Summary:
        Almacena una lista de datos en la base de datos.

        Explanation:
        Itera sobre una lista de datos en formato JSON y los almacena en la base de datos configurada en la aplicación actual. Devuelve una lista con los resultados de la operación de inserción en la base de datos.

        Args:
        - data: Lista de datos tipo json a ser almacenados en la base de datos

        Returns:
        - Lista de resultados de la operación de inserción en la base de datos
    """
    
    _collection = "consultas"
    
    
    def almacenar_lista_datos(self, data):
        database = current_app.config['db']
        lista_result = []
        for item_data in data:
            # print(f"item_data:{str(item_data)}")
            lista_result.append(database[self._collection].insert_one(item_data))
        return lista_result
        