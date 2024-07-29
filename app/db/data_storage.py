
from flask import current_app

class DataStorage:
    
    _collection = "consultas"
    
    
    def almacenar_lista_datos(self, data):
        database = current_app.config['db']
        lista_result = []
        for item_data in data:
            print("item_data:"+str(item_data))
            lista_result.append(database[self._collection].insert_one(item_data))
        return lista_result
        