from collections.abc import Mapping
from typing import Any

import psutil
import subprocess
import sys
import time
import os.path

from model.abstractoutboundinterlayer import AbstractOutboundInterlayer

'''
Since the intention is to refactor the way group analytics data is stored to use
a fully fledged database, instead of refactoring the methods of getting data that already
exist in the frontend's old data parser, just to rewrite it all anyways when switching over,
for now, the model backend interlayer, will just use the methods in the frontend's old
data parser in the interim.

'''

import model.data_parser as data_parser

class MSOInterlayer(AbstractOutboundInterlayer):

    def __init__(self, parent=None):
        super().__init__(parent)

    '''
    Database Queries

    '''



    # Override
    def query_days_from_db(self) -> list[Mapping[str, str, int]]:

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
    Start/Stop VRCGA service

    '''

    # Override
    def start_vrcga_service(self) -> psutil.Process:

        # Get VRCGA Service name/path
        config = data_parser.get_app_config() 
        service_process_name = config["serviceProcessName"]

        service_process = self.is_running(service_process_name)
        if service_process[0]:
            return service_process[1]
        
        service_exe_path = os.getcwd() + config["serviceExePath"]
        run_args = [service_exe_path]
        print(service_exe_path)

        # VRCGA_GUI_TEST
        devcwd = config["DEVserviceCWD"]

        # Make so service doesn't close when frontend is closed
        # Popen args needed differ, depending on OS
        if sys.platform == "win32": # for Windows
            subprocess.Popen(
                run_args,
                cwd=devcwd, # VRCGA_GUI_TEST
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS,
                shell=True
            )
        else: # for POSIX systems (like linux and macOS)
            subprocess.Popen(
                run_args,
                start_new_session=True,
                shell=True
            )
        
        service_process = self.is_running(service_process_name)
        while not service_process[0]:
            time.sleep(1)
            service_process = self.is_running(service_process_name)

        return service_process[1]

    # Override
    def stop_vrcga_service(self, service_proc: psutil.Process):
        try:
            service_proc.terminate()
            print("Backend stopped succesfully")
        except Exception as error:
            print(f"ERROR: Failed to terminate backend process: {error}")
        
        time.sleep(3)
        try:
            if self.is_running(service_proc.name)[0] == True:
                print("Backend Process failed to terminate successfully")
                print("Attempting force kill")
                service_proc.kill()
        except Exception as error:
            print(f"ERROR: Failed to force kill backend process: {error}")

    # Is the VRCGA service running, and if so, what's its process?
    def is_running(self, service_process_name):
        for process in  psutil.process_iter(["name"]):
            if process.info["name"] == service_process_name:
                return (True, process)
        return (False, None)