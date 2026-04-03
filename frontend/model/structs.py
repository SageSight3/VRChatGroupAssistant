'''
While these aren't structs in the literal sense, these classes are meant to
serve the same purpose, as them, so Model is more organized

'''

class OnlineCountTrackerData:

    def __init__(self, online: int, total: int, percent: int, timestamp: str):

        # Inst vars are public, since this class is just meant to be a
        # data container
        self.online_count = online
        self.total_count = total
        self.online_percent = percent
        self.timestamp = timestamp

class Day(object):
    
    def __init__(self, a_date, a_weekday, an_index):
        
        self.date: str = a_date
        self.weekday: str = a_weekday
        self.index: int = an_index