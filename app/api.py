#!/usr/bin/env python

from flask import request, jsonify, Blueprint

from app.db.data_storage import DataStorage
from app.services.data_enricher import DataEnricher
from app.services.procesar_archivo import ProcesarArchivo

routes = Blueprint("api", __name__, url_prefix="/api/v1/")

@routes.route('/', methods=[ 'GET' ])
def todo():
    return "API en funcionamiento"


@routes.route('/cargar_datos_archivo', methods=['POST', 'GET'])
def cargar_datos():
    """
        Summary:
        Handles POST requests to store data from a file.

        Explanation:
        Maneja solicitudes POST para almacenar datos de un archivo. Si el método de solicitud no es POST, devuelve un mensaje de error.
        Si se produce un error al almacenar el archivo, devuelve el mensaje de error. De lo contrario, devuelve los datos almacenados.
        
        Args:
        - None

        Returns:
        - JSON response with status code 400 for errors, 200 for success.
    """
    if request.method != 'POST':
        ## get request
        return jsonify({"status": "Ejecución de API GET" }), 400
    
    file = request.files.getlist('files')
    
    
    dataStorage = DataStorage()
    enricher = DataEnricher()
    procesarArchivo = ProcesarArchivo(dataStorage, enricher)
    resultado = procesarArchivo.run(file)
    if resultado and resultado["status"] == "error":
        return jsonify(resultado), 400
    
    return jsonify(resultado), 200


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 5000), debug=True)
    