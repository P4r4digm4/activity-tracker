from tkinter import Frame, Label, Button
import tkinter as tk
from watch import StopWatch

class TimerWidget(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        self.stopwatch = StopWatch()

        self.time_label = Label(self, text = '00:00:00', font = ("Arial", 24))
        self.time_label.pack()

        self.start_button = Button(self, text="Старт", command = self.start_timer)
        self.start_button.pack(side = tk.LEFT)

        self.stop_button = Button(self, text = "Стоп", command= self.stop_timer, state = tk.DISABLED)
        self.stop_button.pack(side = tk.LEFT)

        self.update_display()

    def start_timer(self):
        start_time = self.stopwatch.start()
        print(f"начало в {start_time}")
        self.start_button.config(state = tk.DISABLED)
        self.stop_button.config(state = tk.NORMAL)

        return start_time

    def stop_timer(self):
        end_time = self.stopwatch.stop()
        print(f"кончил в {end_time}")
        self.start_button.config(state = tk.NORMAL)
        self.stop_button.config(state = tk.DISABLED)

        return end_time

    def update_display (self):
        if self.stopwatch._is_running:
            current_sec = self.stopwatch.get_current_time()

            hours = int(current_sec //3600)
            minutes = int((current_sec % 3600) // 60)
            seconds = int(current_sec % 60)
            self.time_label.config(text = f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        self.after(100, self.update_display)



