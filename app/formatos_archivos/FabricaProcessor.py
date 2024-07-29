from app.formatos_archivos import FileProcessorStrategy
from app.formatos_archivos.CSVProcessor import CSVProcessor
from app.formatos_archivos.JSONLProcessor import JSONLProcessor


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
    def get_strategy( formato ) -> FileProcessorStrategy:
        if formato == "csv":
            return CSVProcessor()
        elif formato == "jsonl":
            return JSONLProcessor()
        else:
            return None