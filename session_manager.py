import datetime

import storage
from models import Activity


class SessionManager:
    def __init__(self):
        self.sessions = []


    def add_session(self, activity: Activity or Old_Activityes) :
        self.sessions.append(activity)

    def get_total_time_for(self, name: str) -> datetime.timedelta:
        total = datetime.timedelta()
        for session in self.sessions:
            if session.name == name:
                total += session.duration
        return total


