#!/usr/bin/env python
import os

from flask import Flask, request, jsonify
from pymongo import MongoClient
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['xls', 'csv', 'png', 'jpeg', 'jpg'])
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../uploads'))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000  # 500 MB
app.config['CORS_HEADER'] = 'application/json'

client = MongoClient("mongo:27017")


def allowedFile(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello Anderson B, from the MongoDB client!\n"

@app.route('/cargar_datos_archivo', methods=['POST', 'GET'])
def cargar_datos():
    
    if request.method == 'POST':
        file = request.files.getlist('files')
        filename = "-"
        for f in file:
            print(f.filename)
            filename = secure_filename(f.filename)
            if allowedFile(filename):
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return jsonify({"status": "success"})
            else:
                return jsonify({"error": "Archivo no permitido -> "+str(filename)}), 400
        
        return jsonify({"status":"error", "error": "No se encontró archivo en la peticion"}), 400
    ## get request
    return jsonify({"status": "Ejecución de API GET" }), 400
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 5000), debug=True)
    