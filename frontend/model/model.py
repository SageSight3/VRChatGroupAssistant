from PySide6.QtCore import QObject

from model.modelbackendinterlayer import ModelBackendInterlayer
from model.structs import *

class Model(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Interlayer object for frontend communication with database and VRCGA service
        self.__interlayer = ModelBackendInterlayer()
        
        # Days hold two vals, one for the date, one for the weekday
        self.__days: list[Day] = []

        # Data for Online Counts Tracker
        self.__online_counts_data = OnlineCountsTrackerData()

        self.inialize_data()

    def inialize_data(self):
        self.update_days()
        self.update_date_online_counts_data(self.__days[0].date)

    def update_days(self):
        # Clear days list for updating
        self.__days.clear()
        
        # Get update days list from backend
        updated_days = self.__interlayer.query_days_from_db()

        for day in updated_days:
            date = day["Date"]
            weekday = day["Weekday"]
            day_data = Day(date, weekday)
            self.__days.append(day_data)

    # Update online counts data with the online and total counts, timestamps, and online percents
    # of a group for the passed in date
    def update_date_online_counts_data(self, date):
        # Get online counts for passed in date, from backend
        new_data = self.__interlayer.query_date_online_counts_data(date)

        online = new_data["Online"]
        total = new_data["Total"]
        timestamps = new_data["Timestamps"]

        self.__online_counts_data.online_counts = online
        self.__online_counts_data.total_counts = total
        self.__online_counts_data.timestamps = timestamps

        # Clear online percents list, before assigning it new data
        self.__online_counts_data.online_percents.clear()

        # Calculate and update online_percents for online counts tracker data
        for index in range(len(timestamps)): # taking the length of timestamps is arbitrary here
            if online[index] <= 0 or total[index] <= 0:
                self.__online_counts_data.online_percents.append(0)
                continue
            an_online_percent = online[index] / total[index]
            an_online_percent = int(round(an_online_percent, 2) * 100)
            self.__online_counts_data.online_percents.append(an_online_percent)



    '''
    Getters

    '''



    def get_days(self):
        return self.__days
    
    def get_online_counts_data(self):
        return self.__online_counts_data







