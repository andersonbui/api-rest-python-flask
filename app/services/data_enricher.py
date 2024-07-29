from app.services.apis_request.items_api_client import ItemsInfoAPIClient

class DataEnricher:
    def __init__(self):
        self.api_clients = [
            ItemsInfoAPIClient(),
            #CategoryInfoAPIClient(),
            # Agrega aquí más clientes de APIs según se necesite
        ]

    def enrich(self, record):
        for client in self.api_clients:
            additional_data = client.fetch_additional_data(record)
            record.update(additional_data)
        return record