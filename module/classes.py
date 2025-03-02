from pathlib import Path

# Document CLass
class Document:
    def __init__(self,file_path: Path):
        self.file_path = file_path


    def print_text(self):
        return self.file_path.read_text('utf-8')
