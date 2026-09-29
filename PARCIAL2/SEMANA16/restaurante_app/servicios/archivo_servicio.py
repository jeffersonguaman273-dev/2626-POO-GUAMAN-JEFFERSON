import json
import os

class ArchivoServicio:
    def __init__(self, base_path: str):
        self.base_path = base_path

    def leer(self, filename: str):
        path = os.path.join(self.base_path, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo {path} no existe")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def escribir(self, filename: str, data):
        path = os.path.join(self.base_path, filename)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
