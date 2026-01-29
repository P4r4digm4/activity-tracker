

import datetime
import time

class StopWatch:

    def __init__(self):
        self._first_start_time = None # первый старт
        self._last_resume_time = None # последний старт

        self._is_running = False
        self._total_elapsed = 0.0
        self._is_paused = False

    def start(self) -> datetime.datetime:
        if self._is_running:
            raise Exception ("Таймер уже запущен")

        self._first_start_time = datetime.datetime.now()
        self._last_resume_time = self._first_start_time
        self._total_elapsed = 0.0
        self._is_paused = False
        self._is_running = True

        return self._first_start_time

    def timeout(self):
        if not self._is_running or self._is_paused:
            raise Exception('таймер не запущен или уже на паузе')

        now = datetime.datetime.now()
        self._total_elapsed += (now - self._last_resume_time).total_seconds()
        self._is_paused = True
        self._is_running = False


    def continue_time(self):
        if not self._is_paused:
            raise Exception('Таймер не на паузе')

        self._last_resume_time = datetime.datetime.now()
        self._is_running = True
        self._is_paused = False

    def stop(self) -> tuple[datetime.datetime, float]:


        if self._is_running == False and self._is_paused == False:
            raise Exception ("Таймер не запущен")


        now = datetime.datetime.now()
        end_time = now
        total_elapsed = self._total_elapsed

        if self._is_running:
            total_elapsed+=(now - self._last_resume_time).total_seconds()

        self._is_paused=False
        self._is_running=False
        self._total_elapsed = 0.0
        self._first_start_time = None
        self._last_resume_time = None

        return end_time, total_elapsed

    def get_current_time(self) -> float:

        if not self._is_running and not self._is_paused:
            return 0.0

        total = self._total_elapsed
        if self._is_running :
            total += (datetime.datetime.now() - self._last_resume_time).total_seconds()
            return total






