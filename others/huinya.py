'''1 уровень. я захожу в него, вписываю название активности,
 нажимаю на кнопку начать, нажимаю на кнопку закончить, он сохраняет дату и время
  начала и окончания активности, трекер запоминает эти данные и сохраняет где то
   ( в отдельную переменную типо dict? или можно добавлять в качестве листа, или
   листа в словаре, типо где название активности будет в качестве ключа,
   а останльное в качестве листа со словарями, типо {activities: [{data: [start, stop]},
    {data2: [start, stop]}] и т.д.
    '''
import datetime

'''
class Activity():
    def _init_(self, name, start_time, end_time):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.duration = end_time - start_time


'''

'''
from tkinter import *
from watch import StopWatch
from dbb import DataBase

def main():

    root = Tk()
    root.title('Timer')
    root.geometry('500x500')
    sw = StopWatch(root)
    sw.place(x = 200, y = 100)
    db = DataBase(sw)

    entry_activity = Entry(width=50)
    entry_activity.place(x=100, y=200)

    def func():
        db.show_start(sw.Start())
        #print(sw.Start())
    start = Button(text='Начать', width=20, command = func)
    start.place(x=100, y=220)


    def func1():
        db.show_stop(sw.Stop())

    stop = Button(text='Завершить', width=20, command = func1)
    stop.place(x=255, y=220)

    reset = Button(text='Сбросить', width=20, command = sw.Reset)
    reset.place(x=100, y=245)

    quit_btn = Button(root, text='Выход', width=20, command = root.quit)
    quit_btn.place(x = 255, y = 245)

    def save_func():
        cur_act = db.data(db.show_message(entry_activity),sw.date_begin, sw.date_break)
        db.json_saves(cur_act)
    save = Button(root, text='Сохранить', width=20, command=save_func)
    save.place(x=255, y=275)

    root.mainloop()





if __name__ == '__main__':
    main()

'''