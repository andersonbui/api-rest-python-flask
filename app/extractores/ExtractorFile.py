import io

class ExtractorGenericoArchivo:
    
    def __init__(self, strategy):
        self.strategy = strategy
    
    def process_file_in_chunks(self, file_stream, chunk_size=1):
        buffer = io.StringIO(file_stream.read().decode('utf-8'))
        incomplete_line = ""
        index_chunk = 0
        while True:
            chunk = buffer.read(chunk_size)
            if not chunk:
                if incomplete_line:
                    processed_chunk, _ = self.strategy.extraer("", incomplete_line, index_chunk)
                    yield processed_chunk
                    
                break
            processed_chunk, incomplete_line = self.strategy.extraer(chunk, incomplete_line, index_chunk)
            index_chunk += 1
            yield processed_chunk
            
    