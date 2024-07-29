from app.processors import FileProcessorStrategy
from app.processors.CSVProcessor import CSVProcessor
from app.processors.JSONLProcessor import JSONLProcessor


class FabricaProcessor:
    """
        Una clase de fábrica para crear estrategias de procesador de archivos basadas en el formato de archivo.

        get_strategy(formato) -> FileProcessorStrategy
            Obtiene la estrategia de procesador de archivos basada en el formato especificado.

        Argumentos:
            formato (str): El formato del archivo para el que se necesita la estrategia de procesador.

        Retorna:
            FileProcessorStrategy: La estrategia de procesador de archivos para el formato especificado, o None si no se encuentra.
    """
    
    @staticmethod
    def getAllowedExtensions():
        return set(['csv', 'text', 'jsonl'])
    
    @staticmethod
    def allowedFile(filename):
        extension_archivo = filename.rsplit('.', 1)[1].lower()
        return '.' in filename and \
            extension_archivo in FabricaProcessor.getAllowedExtensions()

    @staticmethod
    def get_strategy( formato ) -> FileProcessorStrategy:
        if formato == "csv":
            return CSVProcessor()
        elif formato == "jsonl":
            return JSONLProcessor()
        else:
            return None