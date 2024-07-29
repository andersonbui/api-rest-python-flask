from app.extractores.ExtractorFileStrategy import ExtractorFileStrategy
from flask import current_app as app


class ExtractorCSV(ExtractorFileStrategy):
    
    _headers = None
    
    def extraer(self, chunk, incomplete_line, index_chunk):
        lineas = (incomplete_line + chunk).splitlines()
        linea_incompleta = ""
        if(index_chunk == 0):
            self._headers = lineas[0].split(app.config['CSV_SEPARATOR'])
            # ignorar cabecera
            lineas = lineas[1:]
        # la ultima linea puede ser incompleta
        if lineas[-1][-1] != '\n':
            linea_incompleta = lineas[-1]
            lineas = lineas[:-1]
            
            
        rows = [ self.linea_csv_a_diccionario(linea, self._headers) for linea in lineas ]

        return rows, linea_incompleta
    
    def linea_csv_a_diccionario(self, linea, headers):
        return dict(zip(headers, linea.split(app.config['CSV_SEPARATOR'])))