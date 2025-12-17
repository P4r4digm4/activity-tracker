import json
import time
import datetime
from datetime import datetime, timedelta





# первое, что увидит пользователь: предложение заняться активностью и ввести название.

def formating(format):
    formate = str(format)
    return formate


def data(activities, start, stop, time):
    data = {activities:{start:[start, stop, time]}}
    return data


def json_saves(current_activities):
    with open("pipiski.json", "w", encoding = "utf-8") as f:
        cur_active = json.dump(current_activities, f, ensure_ascii= False)
    return f"файл успешно создан {cur_active}"
