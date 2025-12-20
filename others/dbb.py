'''

import json
import time
import datetime
from datetime import datetime, timedelta


class DataBase:
    def __init__(self, parent = None):
        self.parent = parent

    def formating(self, start, stop):
        d = []
        time = timedelta()
        for i in range(0, len(stop)):
            d.append(stop[i] - start[i])
            print(d)
            time = d[0] + time

            print(time, '  ','jopa')


    def data(self, activities, start, stop):
        list_time_act = []
        time = timedelta()
        for i in range(0, len(stop)):
            list_time_act.append(stop[i] - start[i])
            print(list_time_act)
            time = list_time_act[0] + time

            activities = str(activities).strip()
            print(time, '  ', 'jopa')

        data1 = {activities:{start[0].date():[start[0].time(), stop[len(stop)-1].time(), time]}}
        print(data1)
        return str(data1)


    def json_saves(self, current_activities):
        with open("pipiski.json", "a", encoding = "utf-8") as f:
            cur_active = json.dump(current_activities, f, ensure_ascii= False)
        return f"файл успешно создан {cur_active}"

    def show_message(self, entry_activity):
        cur_activity = entry_activity.get()
        return cur_activity

    def show_start(self, date):
        start = date
        print(start)

    def show_stop(self, date):
        stop = date
        print(stop)
'''