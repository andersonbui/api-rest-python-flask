from app.services.apis_request.categories_api_client import CategoryInfoAPIClient
from app.services.apis_request.currencies_api_client import CurrenciesInfoAPIClient
from app.services.apis_request.items_api_client import ItemsInfoAPIClient
from app.services.apis_request.users_api_client import UsersInfoAPIClient

class DataEnricher:
    """
        Summary:
        Enriquece un registro de datos con información adicional de múltiples APIs.

        Explanation:
        Inicializa una lista de clientes de API y enriquece un registro de datos iterando sobre cada cliente para obtener información adicional. Actualiza el registro con la información adicional obtenida y lo devuelve.

        Args:
        - record: El registro de datos al que se le desea añadir información adicional de las APIs

        Returns:
        - El registro de datos enriquecido con la información adicional de las APIs
    """
    
    
    def __init__(self):
        self.api_clients = [
            ItemsInfoAPIClient(),
            CategoryInfoAPIClient(),
            CurrenciesInfoAPIClient(),
            UsersInfoAPIClient(),
            # Agrega aquí más clientes de APIs según se necesite
        ]
        

    def enrich(self, record):
        for client in self.api_clients:
            additional_data = client.fetch_additional_data(record)
            record.update(additional_data)
        return record