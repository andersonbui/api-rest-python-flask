#!/usr/bin/env python
from app.processors.FabricaProcessor import FabricaProcessor
from app.processors.FileProcessor import FileProcessor



class ProcesarArchivo:
    
            # lista_datos = []
    _dataStorage = None
    _enricher = None
    
    def __init__(self, dataStorage, enricher):
        self._dataStorage = dataStorage
        self._enricher = enricher
    
    @staticmethod
    def getExtension(filename):
        return filename.rsplit('.', 1)[1].lower()


    def query_external_api(self, row_list):
        for data in row_list:
            self._enricher.enrich(data)
        return row_list

    def run(self, file):
        """
            Summary:
            Procesa un archivos enviado por parámetro para extraer datos, agrega nuevos datos y almacenarlos en la base de datos.

            Explanation:
            Basado en los datos del archivo pasado por parámetro comprueba las extensiones de archivo, extrae los datos y basado en diferentes estrategias procesa dicho archivo para agregar mas informacion y luego almacenarlos en la base de datos.
            Devuelve un estado de éxito si se almacena el archivo; de lo contrario, devuelve un mensaje de error.
                
            Args:
            - file: El archivo cargado por la petición HTTP

            Returns:
            - Respuesta JSON con estado "éxito" si el archivo está almacenado, o con estado "error" y mensaje de error si hay problemas.
        """
        
        for f in file:
            if not FabricaProcessor.allowedFile(f.filename):
                extension = f.filename.split('.')[1].upper()
                extensiones_permitidas = ', '.join(FabricaProcessor.getAllowedExtensions())
                return {"status": "error", "error": f"Extension {extension} no permitida. Solo se permiten {extensiones_permitidas}"}
            
            try:
                chunk_size = 100 * 1
                #file_stream = io.StringIO(f.stream.read().decode('utf-8'))
                extension_archivo = f.filename.rsplit('.', 1)[1].lower()
                un_processor = FabricaProcessor.get_strategy(extension_archivo)
                processor = FileProcessor(un_processor)
                for row in processor.process_file_in_chunks(f.stream, chunk_size):
                    print(row)
                    if(row == "" or row is None or row == []):
                        continue
                    
                    result_api = self.query_external_api(row)
                    data = self._dataStorage.almacenar_lista_datos(result_api)
                    
                    # print("result_api:"+str(result_api))
                    # lista_datos.append(
                    #     json.loads(json.dumps(result_api, default=lambda o: None))
                    # )
                
            except Exception as e:
                return {"status": "error", "error": str(e)}
            
            return {"status": "success"}
        
        return {"status":"error", "error": "No se encontró archivo en la petición"}
