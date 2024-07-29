#!/usr/bin/env python
import os
import io
import requests

from flask import request, jsonify, Blueprint, current_app
# from pymongo import MongoClient
from werkzeug.utils import secure_filename
from app.processors.FabricaProcessor import FabricaProcessor
from app.processors.FileProcessor import FileProcessor
from app.processors.CSVProcessor import CSVProcessor

ALLOWED_EXTENSIONS = set(['xls', 'csv', 'text', 'jsonl'])

routes = Blueprint("api", __name__, url_prefix="/api/v1/")


def getExtension(filename):
    return filename.rsplit('.', 1)[1].lower()

def allowedFile(filename):
    return '.' in filename and \
        getExtension(filename) in ALLOWED_EXTENSIONS

@routes.route('/', methods=[ 'GET' ])
def todo():
    db = None
    try:
        db = current_app.config['db']
    except:
        return "Server not available"
    return "Collecciones de bbd: " + str(db.list_collection_names())

def query_external_api(data):
    api_url = "https://webhook.site/cd6880ef-8705-47f4-a00b-770a41a60ffb"
    #response = requests.post(api_url, json=data)
    #return response

def almacenar_archivo(file):
    """
        Summary:
        Almacena archivos cargados de forma segura.

        Explanation:
        Almacena los archivos cargados de forma segura. Comprueba las extensiones de archivo, crea una carpeta de carga si no existe y guarda el archivo.
        Devuelve un estado de éxito si se almacena el archivo; de lo contrario, devuelve un mensaje de error.
            
        Args:
        - file: El archivo cargado por la petición HTTP

        Returns:
        - Respuesta JSON con estado "éxito" si el archivo está almacenado, o con estado "error" y mensaje de error si hay problemas.
    """
    
    # filename = "-"
    lista_datos = []
    for f in file:
        if not allowedFile(f.filename):
            extension = f.filename.split('.')[1].upper()
            extensiones_permitidas = ', '.join(ALLOWED_EXTENSIONS)
            return {"status": "error", "error": f"Extension {extension} no permitida. Solo se permiten {extensiones_permitidas}"}
        
        try:
            chunk_size = 100 * 1
            #file_stream = io.StringIO(f.stream.read().decode('utf-8'))
            un_processor = FabricaProcessor.get_strategy(getExtension(f.filename))
            processor = FileProcessor(un_processor)
            for row in processor.process_file_in_chunks(f.stream, chunk_size):
                print(row)
                if(row == "" or row is None or row == []):
                    continue
                query_external_api(row)
                lista_datos.append(row)
                #break
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
        
        return {"status": "success", "filename": lista_datos}
    
    return {"status":"error", "error": "No se encontró archivo en la petición"}

def procesar_archivo_grande_por_fragmentos(file):
    """
        Summary:
        Procesa un archivo de forma segura.

        Explanation:
        Procesa un archivo de forma segura. Carga el archivo de la base de datos y lo procesa. Devuelve un estado de validez si se procesa el archivo; de lo contrario, devuelve un mensaje de error.  

        Args:
        - filename: El archivo cargado por la petición HTTP

        Returns:
        - Respuesta JSON con estado "éxito" si el archivo está procesado, o con estado "error" y mensaje de error si hay problemas.
    """
    try:
        chunk_size = 1024 * 1024
        file_stream = io.StringIO(file.stream.read().decode('utf-8'))
        
        
        
                
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
    

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
    resultado = almacenar_archivo(file)
    if resultado and resultado["status"] == "error":
        return jsonify(resultado), 400
    
    filename = resultado["filename"]
    #procesar_archivo(app.config['UPLOAD_FOLDER'] + '/' + filename)

    return jsonify(resultado), 200


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 5000), debug=True)
    