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

        self.timeout_button = Button(self, text='Пауза', command=self.timeout_timer)
        self.timeout_button.pack(side=tk.LEFT)

        self.continue_button = Button(self, text="Продолжить", command=self.continue_timer,
                                      state=tk.DISABLED)
        self.continue_button.pack(side=tk.LEFT)

        self.update_display()

    def start_timer(self):
        start_time = self.stopwatch.start()
        print(f"начало в {start_time}")
        self.start_button.config(state = tk.DISABLED)
        self.stop_button.config(state = tk.NORMAL)
        self.timeout_button.config(state = tk.NORMAL) #чтобы на паузу можно было нажать!
        self.continue_button.config(state = tk.DISABLED)

        return start_time

    def timeout_timer(self):
        try:
            self.stopwatch.timeout()
            self.timeout_button.config(state = tk.DISABLED)
            self.continue_button.config(state = tk.NORMAL)
            self.stop_button.config(state = tk.DISABLED)
        except Exception as e:
            print(f'Ошибка паузы: {e}')

    def continue_timer(self):
        try:
            self.stopwatch.continue_time()
            self.continue_button.config(state = tk.DISABLED)
            self.timeout_button.config(state = tk.NORMAL)
            self.stop_button.config(state = tk.NORMAL)
        except Exception as e:
            print(f'Ошибка продолжения: {e}')



    def stop_timer(self):
        end_time, total_elapsed = self.stopwatch.stop()
        print(f"кончил в {end_time}, отработал{total_elapsed}c.")

        self.start_button.config(state = tk.NORMAL)
        self.stop_button.config(state = tk.DISABLED)
        self.timeout_button.config(state = tk.DISABLED)
        self.continue_button.config(state = tk.DISABLED)

        return end_time, total_elapsed

    def update_display (self):
        if self.stopwatch._is_running:
            current_sec = self.stopwatch.get_current_time()

            hours = int(current_sec //3600)
            minutes = int((current_sec % 3600) // 60)
            seconds = int(current_sec % 60)
            self.time_label.config(text = f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        self.after(100, self.update_display)



