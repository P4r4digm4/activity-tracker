from tkinter import  Tk, Entry, Button, StringVar
from timerwidget import TimerWidget
from session_manager import SessionManager
from storage import JsonStorage
from models import Activity
import datetime

class App:
    def __init__(self):

        self.root = Tk()
        self.root.title("Трекер Активности")
        self.root.geometry("500x500")

        self.session_manager = SessionManager()
        self.storage = JsonStorage()

        self.timer_widget = TimerWidget(self.root)
        self.timer_widget.place(x = 150 , y = 50)

        self.activity_name_var = StringVar()
        self.name_entry =  Entry(self.root, textvariable=self.activity_name_var, width = 40)
        self.name_entry.place(x = 100, y = 200)
        self.name_entry.insert(0, "Введите название активности")

        self.save_button = Button(self.root, text = "Сохранить активность",
                                  command = self.save_activity, width= 25)
        self.save_button.place(x = 150, y = 230)

        self.current_session_start = None

        self.timer_widget.start_button.config(command = self.on_start_clicked)
        self.timer_widget.stop_button.config(command = self.on_stop_clicked)

    def on_start_clicked(self):
        # вызывается при нажатии старт
        '''Работа старта: функция timer.widget.start_timer() вызывает функцию StopWatch.start()
            StopWatch.start() - флагу в классе StopWatch(SW) - присваивается значение True
            присваевает и возвращает в переменной результат функции datatime.datatime.now()
        timer.widget.start_timer() возвращает значение из SW.start
        '''
        self.current_session_start = self.timer_widget.start_timer()
        # print(f"Логгирование  - self.current_session_start - {self.current_session_start} -- on_start_clicked")

    def on_stop_clicked(self):
        # вызывается при нажатии стоп
        self.timer_widget.stop_timer()
        ''' timer_widget.stop_timer() возвращает время окончания. 
        Вызывает SW.stop, тоже самое что и sw.start - но наоборот
        
        '''

    def save_activity(self):
        '''
        Сохраняет активность путем создания экземпляра класса Activity
        (отвечает за структуру данных)
        '''
        print(f"Логгирование - self.current_session_start - {self.current_session_start} --save_activity")

        if self.current_session_start is None:
            #print("Ошибка! Сначала запустите таймер")
            return

        name = self.activity_name_var.get()
        if not name or name == "Введите название активности":
           # print("Ошибка! Введите название активности.")
            return

        end_time = datetime.datetime.now()

        new_activity = Activity(name = name,
                                start = self.current_session_start,
                                end = end_time)

        self.session_manager.add_session(new_activity)
        # добавляет активность
        self.storage.save_all(self.session_manager.sessions)
        # сохраняет ее

       # print(f"Активность {name} сохранена")
       # print(f"Начало: {self.current_session_start}")
       # print(f"Окончание: {end_time}")
       # print(f"Продолжительность: {new_activity.duration}")

        self.current_session_start = None
        self.activity_name_var.set("")

    def run (self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()

