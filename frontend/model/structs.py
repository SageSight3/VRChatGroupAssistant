'''
While these aren't structs in the literal sense, these classes are meant to
serve the same purpose, as them, so Model is more organized

'''

class OnlineCountsTrackerData:

    def __init__(self):

        # Inst vars are public, since this class is just meant to be a
        # data container
        self.online_counts: list[int] = []
        self.total_counts: list[int] = []
        self.online_percents: list[int] = []
        self.timestamps: list[str] = []

class Day(object):
    
    def __init__(self, a_date, a_weekday):
        
        self.date: str = a_date
        self.weekday: str = a_weekday