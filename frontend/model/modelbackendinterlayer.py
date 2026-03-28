from collections.abc import Mapping
from typing import Any

from model.abstractinterlayer import AbstractInterlayer

'''
Since the intention is to refactor the way group analytics data is stored to use
a fully fledged database, instead of refactoring the methods of getting data that already
exist in the frontend's old data parser, just to rewrite it all anyways when switching over,
for now, the model backend interlayer, will just use the methods in the frontend's old
data parser in the interim.

'''

import data_parser

class ModelBackendInterlayer(AbstractInterlayer):

    def __init__(self, parent=None):
        super().__init__(parent)

    '''
    Database Queries

    '''



    # Override
    def query_days_from_db(self) -> list[Mapping[str, str]]:

        # Get dates and weekdays for every entry in logs
        days = data_parser.get_activity_log_data(ret_dates=True, ret_weekdays=True)

        # Create a list of unique days
        sorted_days = []
        for index in range(len(days["Dates"])): # Dates key is arbitary here
            date = days["Dates"][index]
            weekday = days["Weekdays"][index]
            day = {"Date": date, "Weekday": weekday}
            if day not in sorted_days:
                sorted_days.append(day)

        # Reverse the list, so the most recent day is the first element
        sorted_days.reverse()

        return sorted_days

    # Override
    def query_date_online_counts_data(self, date) -> list[Mapping[str, Any]]:

        data = data_parser.get_activity_log_data(
            date, 
            ret_log_entry_times=True, 
            ret_online_member_counts=True,
            ret_group_total_member_counts=True
        )

        organized_data = []

        for index in range(len(data["LogEntryTimes"])): # LogEntryTimes key is arbitary here
            datapoint = {
                "Online": data["OnlineMemberCounts"][index],
                "Total": data["GroupTotalMemberCounts"][index],
                "Timestamp": data["LogEntryTimes"][index]
            }
            organized_data.append(datapoint)

        return organized_data


    '''
    Config and Status Queries

    '''



    '''
    Inbound Communications from VRCGA Service

    '''



    '''
    Oubound Communication to VRCGA Service

    '''