# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - Anderson Buitron
"""

import contextlib
import os
from app.db.mongodb import MongoBDClient

from flask import Flask

from app.api import routes

def create_app(test_config=None):
    """
        Create and configure the Flask application.
        Info: https://flask.palletsprojects.com/es/main/tutorial/factory/
        
        Args:
            test_config (dict, optional): Configuration settings for testing purposes. Defaults to None.

        Returns:
            Flask: The configured Flask application.
    """
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('FLASK_SECRET_KEY'),
        MONGODB_STRING_CONNECTION=os.environ.get('MONGODB_STRING_CONNECTION'),
        MONGODB_DATABASE_NAME=os.environ.get('MONGODB_DATABASE_NAME'),
        MAX_CONTENT_LENGTH = 100000 * 1000 * 1000,  # 100000 MB
        CORS_HEADER = 'application/json',
        TESTING  = True,
        CSV_SEPARATOR  = os.environ.get('CSV_SEPARATOR', ',')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        

    # ensure the instance folder exists
    with contextlib.suppress(OSError):
        os.makedirs(app.instance_path)

    db_name = app.config['MONGODB_DATABASE_NAME']
    str_con = app.config['MONGODB_STRING_CONNECTION']
    mongo_client = MongoBDClient(str_con, db_name)
    
    # Guardar la conexión en el contexto de la aplicación
    app.config['db'] = mongo_client.get_db()
    
    # Importar y registrar rutas
    app.register_blueprint(routes)
    
    return app

