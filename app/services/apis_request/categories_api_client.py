
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient

class CategoryInfoAPIClient(BaseAPIClient):
    
    def fetch_additional_data(self, record):
        identifier = record.get('site') + record.get('id')
        api_url = f"https://dominio.co/items/{identifier}"
        response = requests.get(api_url)
        return {
            "price": response.json().get('price'),
            "start_time": response.json().get('date_created'),
        }

