from app.formatos_archivos.FileProcessorStrategy import FileProcessorStrategy
from flask import current_app as app

class CSVProcessor(FileProcessorStrategy):
    
    def process(self, chunk, incomplete_line):
        lineas = (incomplete_line + chunk).splitlines()
        linea_incompleta = ""
        # la ultima linea puede ser incompleta
        if lineas[-1][-1] != '\n':
            linea_incompleta = lineas[-1]
            lineas = lineas[:-1]
        rows = [ linea.split(app.config['CSV_SEPARATOR']) for linea in lineas ]

        return rows, linea_incompleta