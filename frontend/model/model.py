from PySide6.QtCore import QObject, Signal

from model.modelbackendinterlayer import ModelBackendInterlayer
from model.structs import *

class Model(QObject):

    updatedSelectedDay = Signal(object)
    refreshedDaysList = Signal(list, int) # updated days list, updated index of selected day
    refreshedOnlineCountsTrackerData = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Interlayer object for frontend communication with database and VRCGA service
        self.__interlayer = ModelBackendInterlayer()
        
        # Days hold two vals, one for the date, one for the weekday
        self.__days: list[Day] = []
        self.__selected_day = Day("", "", 0)
        self.__online_counts_data: list[OnlineCountTrackerData] = []
        
        # Assign initial values to data
        self.update_days()
        self.update_selected_day(0)
        self.update_date_online_counts_data()


    '''
    Data Update Methods

    '''


    def update_data(self):
        self.update_days()
        self.update_date_online_counts_data()

    def update_days(self):
        # Clear days list for updating
        self.__days.clear()
        
        # Get update days list from backend
        updated_days = self.__interlayer.query_days_from_db()

        # For finding the new index of selected day in the updated dates list
        selected_day_new_index = None

        index = 0 # To guarantee parity with item data in days lists in views
        for day in updated_days:
            date = day["Date"]
            weekday = day["Weekday"]
            day_data = Day(date, weekday, index)
            self.__days.append(day_data)

            if self.__selected_day.date == date:
                selected_day_new_index = index

            index = index + 1

        # If the old selected day isn't found in the updated days list, the selected day should be set reset
        if selected_day_new_index == None:
            selected_day_new_index = 0

        self.refreshedDaysList.emit(self.__days, selected_day_new_index)

    # Update online counts data with the online and total counts, timestamps, and online percents
    # of a group for the passed in date
    def update_date_online_counts_data(self):
        # Clear existing online counts tracker data
        self.__online_counts_data.clear()

        # Get online counts for passed in date, from backend
        new_data = self.__interlayer.query_date_online_counts_data(self.__selected_day.date)

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

        self.refreshedOnlineCountsTrackerData.emit(self.__online_counts_data)

    def update_selected_day(self, index):
        if index == None:
            return
        self.__selected_day = self.__days[index]
        self.updatedSelectedDay.emit(self.__selected_day)


    '''
    Getters

    '''


    def get_days(self):
        return self.__days
    
    def get_online_counts_data(self):
        return self.__online_counts_data







