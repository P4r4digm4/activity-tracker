import datetime

class Activity:
    def __init__(self, name: str, start: datetime.datetime, end: datetime.datetime,
                 duration_seconds: float = None):

        self.name = name.strip()
        self.start = start
        self.end = end

        if duration_seconds is not None:
            self.duration = datetime.timedelta(seconds = duration_seconds)
        else:
            self.duration = end - start


    @classmethod
    def from_dict(cls, data: dict):

        '''
                с помощью fromisoformat() мы обратно превращаем наши данные в datetime.datetime,
                а затем присваиваем значения с новым типом, старым переменным.

        '''
        start = datetime.datetime.fromisoformat(data['start'])
        end = datetime.datetime.fromisoformat(data['end'])
        return cls(name = data['name'], start = start, end = end)

    def to_dict(self):
        return {
            "name": self.name,
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
            "duration_seconds": self.duration.total_seconds()

        }