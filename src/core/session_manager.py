import os
import zipfile
from pathlib import Path
from typing import Optional

class Manager:

    def __init__(self, sessions_root = "../user/sessions"):
        self.sessions_dir = Path(sessions_root).resolve()
        os.makedirs(self.sessions_dir, exist_ok=True)

    def extract_archieve(self, zip_path):
        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(self.sessions_dir)
            return True, f"Сессии сохранены в {self.sessions_dir}"
        except Exception as e:
            return False, f"Ошибка: {str(e)}"
    
    def get_sessions_list(self) -> list[str]:
        return [f.name for f in self.sessions_dir.iterdir() if f.is_dir()]