from typing import List
from pathlib import Path
import shutil


class Parser:

    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path, "r") as rd: return rd

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext)
        with open(full_path, "w") as file:
            return file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest/path.relative_to(source))


class ResourceParser(Parser):
    exstensions: List[str] = [".jpg", ".png", ".gif", ".css", "html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
