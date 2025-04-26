from __future__ import annotations
import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> CleanUpFile:
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        if self.file:
            self.file.close()
        file_path = os.path.abspath(self.filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        return False
