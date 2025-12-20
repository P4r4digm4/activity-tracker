from tkinter import *
from tkinter import ttk

import time
import datetime


class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()

        self._date_running = 0
        self.date_begin = []
        self.date_break = []

        self.makeWidgets()

    def date_start(self):
        self.date_begin.append(datetime.datetime.now())
        return self.date_begin

    def date_stop(self):
        self.date_break.append(datetime.datetime.now())
        print(self.date_break)
        return self.date_break


    def save_time(self, time):
        pass



    def makeWidgets(self):
        l = ttk.Label(self, textvariable=self.timestr, font = 100)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=True, pady=2, padx=2)

    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        minutes = int(elap / 60)
        hours = int(minutes / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d:%02d' % (hours, minutes, seconds, hseconds))
        #self.save_time([hours, minutes, seconds])

    def Start(self):
        if not self._running and not self._date_running:
            self.date_start()
            self._date_running +=1
            print('стартовало')


        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

        return self.date_begin[0]


    def Stop(self):
        if self._running and self._date_running:
            self.date_stop()
            self._date_running = 0

        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

            print('stop', datetime.datetime.now())
        return self.date_break[0]

    def Reset(self):
        #self.date_stop()

        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)