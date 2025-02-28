# Document CLass
from pathlib import Path

class Document:
    def __init__(self,file_path: Path):
        self.file_path = file_path


def print_text(self):
    return Path.read_text(self.file_path)
