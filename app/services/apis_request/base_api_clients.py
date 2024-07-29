
class BaseAPIClient:
    """
        Summary:
        Clase base para clientes de API.

        Explanation:
        Define un método abstracto para obtener datos adicionales de forma externa basados en datos enviados por parámetro. Las subclases deben implementar este método para proporcionar la funcionalidad específica de la API.

        Raises:
        - NotImplementedError: Debe ser lanzado por las subclases si no implementan el método fetch_additional_data.
    """
    
    def fetch_additional_data(self, record):
        raise NotImplementedError("Subclasses must implement fetch_additional_data method.")
