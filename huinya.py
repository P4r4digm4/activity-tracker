'''1 уровень. я захожу в него, вписываю название активности,
 нажимаю на кнопку начать, нажимаю на кнопку закончить, он сохраняет дату и время
  начала и окончания активности, трекер запоминает эти данные и сохраняет где то
   ( в отдельную переменную типо dict? или можно добавлять в качестве листа, или
   листа в словаре, типо где название активности будет в качестве ключа,
   а останльное в качестве листа со словарями, типо {activities: [{data: [start, stop]},
    {data2: [start, stop]}] и т.д.
    '''
import datetime
abc = []

class Uwu():
    def __init__(self, parent = None):
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        #self.timestr = StringVar()

        self._date_running = 0
        self.date_begin = []
        self.date_break = []

        #self.makeWidgets()

    def date_start(self):
        self.date_begin.append(datetime.datetime.now())
        return self.date_begin[0]

a = Uwu()
print(a.date_start())

