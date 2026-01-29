from models import Activity
import json
import datetime

class JsonStorage:

    def __init__(self, filename: str = "activities.json"):
        self.filename = filename

    def save_all(self, sessions: list):



        data_to_save = [session.to_dict() for session in sessions]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump((data_to_save ), f, ensure_ascii= False, indent = 2)

    def load_all(self) -> list:
        try:
            with open(self.filename, 'r', encoding = 'utf - 8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print('Ошибка: файл поврежден, создам новый.')
            return []


