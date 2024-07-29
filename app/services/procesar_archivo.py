#!/usr/bin/env python
from app.processors.FabricaProcessor import FabricaProcessor
from app.processors.FileProcessor import FileProcessor



class ProcesarArchivo:
    """
        Summary:
        Extrae los datos de un archivo, los enriquece y los almacena en una base de datos.

        Explanation:
        Comprueba las extensiones de archivo, extrae los datos del archivo permitido, los enriquece y los almacena en una base de datos.
        Args:
        - file: Objeto que representa un archivo para procesar.

        Returns:
        - Respuesta JSON con estado "éxito" si el archivo está completamente procesado, o con estado "error" y mensaje de error si hay problemas.
    """
    
    _data_storage = None
    _enricher = None
    
    def __init__(self, data_storage, enricher):
        self._data_storage = data_storage
        self._enricher = enricher
    

    def enriquecer_datos(self, row_list):
        """
            Summary:
            Enriquecimiento de datos basado en un objeto decorador.

            Explanation:
            Itera sobre una lista de datos y los enriquece cada dato utilizando un enriquecedor externo. Devuelve la lista de datos enriquecida.

            Args:
            - row_list: Lista de datos a ser enriquecidos

            Returns:
            - La lista de datos enriquecida con datos adicionales agregados por objeto decorador
        """
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
            # NO procesar archivo si la extension no es permitida
            if not FabricaProcessor.allowedFile(f.filename):
                extension = f.filename.split('.')[1].upper()
                extensiones_permitidas = ', '.join(FabricaProcessor.getAllowedExtensions())
                return {"status": "error", "error": f"Extension {extension} no permitida. Solo se permiten {extensiones_permitidas}"}
            
            try:
                # tamaño del segmento de archivo
                chunk_size = 10 * 1024
                # extraer extension de archivo
                extension_archivo = f.filename.rsplit('.', 1)[1].lower()
                # obtener estrategia de acuerdo a extensión
                un_processor = FabricaProcessor.get_strategy(extension_archivo)
                processor = FileProcessor(un_processor)
                for row in processor.process_file_in_chunks(f.stream, chunk_size):
                    # no procesar si la fila es vacía
                    if(row == "" or row is None or row == []):
                        continue
                    
                    result_api = self.enriquecer_datos(row)
                    # Almacenar datos enriquecidos
                    self._data_storage.almacenar_lista_datos(result_api)
                    
                    # print("result_api:"+str(result_api))
                    # lista_datos.append(
                    #     json.loads(json.dumps(result_api, default=lambda o: None))
                    # )
                
            except Exception as e:
                return {"status": "error", "error": str(e)}
            
            return {"status": "success"}
        
        return {"status":"error", "error": "No se encontró archivo en la petición"}
