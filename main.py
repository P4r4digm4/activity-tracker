from tkinter import  Tk, Button, StringVar, ttk
from timerwidget import TimerWidget
from session_manager import SessionManager
from storage import JsonStorage
from models import Activity


class App:
    def __init__(self):

        self.root = Tk()
        self.root.title("Трекер Активности")
        self.root.geometry("500x500")

        self.session_manager = SessionManager()
        self.storage = JsonStorage()

        self.total_elapsed_seconds = None

        self.timer_widget = TimerWidget(self.root)
        self.timer_widget.place(x = 150 , y = 50)


        #здесь строка ввода названия активности как я понял была
        # self.activity_name_var = StringVar()
        # self.name_entry =  Entry(self.root, textvariable=self.activity_name_var, width = 40)
        # self.name_entry.place(x = 100, y = 200)
        # self.name_entry.insert(0, "Введите название активности")

        #self.history = self.view_history()


        self.load_history()

        self.activity_name_var = StringVar()
        self.combo = ttk.Combobox(self.root, values = self.view_history(), width=37, textvariable=self.activity_name_var)
        self.combo.set("Введите название активности")
        self.combo.place(x = 100, y = 200)

        self.save_button = Button(self.root, text = "Сохранить активность",
                                  command = self.save_activity, width= 33)
        self.save_button.place(x = 100, y = 225)

        self.current_session_start = None

        self.timer_widget.start_button.config(command = self.on_start_clicked)
        self.timer_widget.stop_button.config(command = self.on_stop_clicked)

        self.end_time = None


        self.view_history_button = Button(self.root, text = 'Посмотреть историю',
                                         command = self.view_history, width=33)
        self.view_history_button.place(x = 100, y = 250)


    def load_history(self):
        ''' Загружает историю в session_manager'''
        history_data = self.storage.load_all()
        for item in history_data:
            activity  = Activity.from_dict(item)
            self.session_manager.add_session(activity)

    def view_history(self):
        '''Показывает историю для выпадающего списка.'''
        history = self.storage.load_all()
        name_session = []
        for i in range (len(history)):
           name_session.append(history[i]['name'])
        return name_session

    def on_start_clicked(self):
        # вызывается при нажатии старт
        '''
                Работа старта: функция timer.widget.start_timer() вызывает функцию
                StopWatch.start()
                StopWatch.start() - флагу в классе StopWatch(SW) - присваивается
                значение True
                присваивает и возвращает в переменной результат функции
                datatime.datatime.now()
                timer.widget.start_timer() возвращает значение из SW.start
        '''




        self.current_session_start = self.timer_widget.start_timer()

        self.end_time = None
        self.total_elapsed_seconds = None
        print(f"Логгирование  - self.current_session_start - {self.current_session_start} -- on_start_clicked")

    def on_stop_clicked(self):
        # вызывается при нажатии стоп
        '''
                timer_widget.stop_timer() возвращает время окончания.
                Вызывает SW.stop, то же самое что и sw.start - но наоборот
        '''
        self.end_time, self.total_elapsed_seconds = self.timer_widget.stop_timer()
        print(f"Логгирование - total_elapsed: {self.total_elapsed_seconds}, on stop clicked.")


    def save_activity(self):

        '''
                Сохраняет активность путем создания экземпляра класса Activity
                (отвечает за структуру данных)
        '''

        print(f"Логгирование - self.current_session_start - {self.current_session_start} --save_activity")

        if self.current_session_start is None:
            print("Ошибка! Сначала запустите таймер")
            return

        name = self.activity_name_var.get()
        if not name or name == "Введите название активности":
            print("Ошибка! Введите название активности.")
            return

        # if self.total_elapsed_seconds is None:
        #     print("Ошибка: не найдено время работы!")
        #     return

        # Проверка на то была ли нажата кнопка "стоп". Раньше из за этого при нажатой кнопке стоп, и
        # при нажатии спустя время "сохранить активность", сохранялось текущее время, а не время нажатия кнопки
        # "стоп"
        if self.end_time is None or self.total_elapsed_seconds is None:
            self.end_time, self.total_elapsed_seconds = self.timer_widget.stop_timer()


        new_activity = Activity(name = name,
                                start = self.current_session_start,
                                end = self.end_time,
                                duration_seconds= self.total_elapsed_seconds)

        self.session_manager.add_session(new_activity)
        self.storage.save_all(self.session_manager.sessions)

        print(f"Активность {name} сохранена")
        print(f"Начало: {self.current_session_start}")
        print(f"Окончание: {self.end_time}")
        print(f"Продолжительность: ------------------- {new_activity.duration}")

        self.current_session_start = None
        self.end_time = None
        self.total_elapsed_seconds = None
        self.activity_name_var.set("")


    def run (self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()

