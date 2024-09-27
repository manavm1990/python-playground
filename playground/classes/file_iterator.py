from pathlib import Path


class FileIterator:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.file = Path.open(file_path)

    def __iter__(self) -> "FileIterator":
        return self

    def __next__(self) -> str:
        line = self.file.readline()
        if line == "":
            self.file.close()
            raise StopIteration
        return line.strip()
