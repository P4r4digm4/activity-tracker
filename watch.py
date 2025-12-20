

import datetime
import time

class StopWatch:

    def __init__(self):
        self._start_time = None
        self._is_running = False

    def start(self) -> datetime.datetime:
        if self._is_running:
            raise Exception ("Таймер уже запущен")
        self._is_running = True
        self._start_time = datetime.datetime.now()
        return self._start_time

    def stop(self) -> datetime.datetime:
        if self._is_running == False:
            raise Exception ("Таймер еще не запущен")
        if self._is_running:
            self._is_running = False
            end_time = datetime.datetime.now()
            return end_time

    def get_current_time(self) -> float:
        if self._is_running:
            return (datetime.datetime.now() - self._start_time).total_seconds()
        return 0.0






