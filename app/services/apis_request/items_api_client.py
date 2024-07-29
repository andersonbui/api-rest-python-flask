
import requests

from app.services.apis_request.base_api_clients import BaseAPIClient


class ItemsInfoAPIClient(BaseAPIClient):
    
    def fetch_additional_data(self, record):
        identifier = record.get('site') + record.get('id')
        api_url = f"https://rocketchatdev.keos.co/items/{identifier}"
        response = requests.get(api_url)
        return {
            "price": response.json().get('price'),
            "start_time": response.json().get('date_created'),
            "category_id": response.json().get('category_id'),
            "currency_id": response.json().get('currency_id'),
            "seller_id": response.json().get('seller_id'),
        }
