import json
from app.processors.FileProcessorStrategy import FileProcessorStrategy

class JSONLProcessor(FileProcessorStrategy):
    
    def process(self, chunk, incomplete_line):
        lineas = (incomplete_line + chunk).splitlines()
        linea_incompleta = ""
        # la ultima linea puede ser incompleta
        if lineas[-1][-1] != '\n':
            linea_incompleta = lineas[-1]
            lineas = lineas[:-1]
        rows = [ list(json.loads(linea).values()) for linea in lineas if linea ]

        return rows, linea_incompleta