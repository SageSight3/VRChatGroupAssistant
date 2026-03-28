from PySide6.QtCore import QObject, Signal

from model.modelbackendinterlayer import ModelBackendInterlayer
from model.structs import *

class Model(QObject):

    selectedDateChanged = Signal()
    refreshedDaysList = Signal(list)
    refreshedOnlineCountsTrackerData = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Interlayer object for frontend communication with database and VRCGA service
        self.__interlayer = ModelBackendInterlayer()
        
        # Days hold two vals, one for the date, one for the weekday
        self.__days: list[Day] = []
        self.update_days()

        self.__selected_day = self.__days[0]
        
        # Data for Online Counts Tracker
        self.__online_counts_data: list[OnlineCountTrackerData] = []
        self.update_date_online_counts_data(self.__selected_day.date)

    def update_data(self):
        self.update_days()
        self.update_date_online_counts_data(self.__selected_day.date)

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

        self.refreshedDaysList.emit(self.__days)

    def update_selected_day(self, index):
        self.__selected_day = self.__days[index]
        self.selectedDateChanged.emot()

    # Update online counts data with the online and total counts, timestamps, and online percents
    # of a group for the passed in date
    def update_date_online_counts_data(self, date):
        # Clear existing online counts tracker data
        self.__online_counts_data.clear()

        # Get online counts for passed in date, from backend
        new_data = self.__interlayer.query_date_online_counts_data(date)

        # Calculate and update online_percents for online counts tracker data
        for datapoint in new_data: # taking the length of timestamps is arbitrary here

            online = datapoint["Online"]
            total = datapoint["Total"]
            timestamp = datapoint["Timestamp"]
            
            percent = 0
            
            # If total or online is less than 0, than we know that log had an error
            # If online is 0, then percent will be 0 anyways
            # If total is 0, would be a divide by 0 error aka we know there was an error
            # in the log. So only calculate percent if online and total are greater than 0
            # Online will never exceed total
            if online > 0 and total > 0:
                percent_raw_val = online/total
                percent = int(round(percent_raw_val, 2) * 100)

            an_online_count_datapoint = OnlineCountTrackerData(online, total, percent, timestamp)
            self.__online_counts_data.append(an_online_count_datapoint)

        self.refreshedOnlineCountsTrackerData.emit()



    '''
    Getters

    '''



    def get_days(self):
        return self.__days
    
    def get_online_counts_data(self):
        return self.__online_counts_data







