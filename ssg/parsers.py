from typing import List
from pathlib import Path
import shutil

class Parser:
    def __init__(self, source, dest):
        self.extensions = []

    def valid_extension(self, extension):
        return extension in self.extensions
    
    def parse(self, path, source, dest):
        path = Path()
        source = Path()
        dest = Path()
        raise NotImplementedError
    def read(self, path):
        with open(path, 'r') as reader1:
            return reader1.read()  
    def write(self, path, dest, content, ext =".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, 'w') as writer:
            writer.write(content)     
    def copy(self, path, source, dest):
        shutil.copy2(path, (self.dest / path.relative_to(self.source)))
    def valid_extension(extension):

class ResourceParser(Parser):
    def __init__(self, source, dest):
        self.extensions = list(".jpg", ".png", ".gif", ".css", ".html")
    def copy(self, path, source, dest):
        super().copy(path, source, dest)