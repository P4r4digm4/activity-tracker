import datetime

def p():
    pass
class Activity:
    def __init__(self, name: str, start: datetime.datetime, end: datetime.datetime):
        self.name = name.strip()
        self.start = start
        self.end = end

        self.duration = end - start

    def to_dict(self):
        return{
            "name": self.name,
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
            "duration_seconds": self.duration.total_seconds()
        }