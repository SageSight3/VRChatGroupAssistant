from PySide6.QtCore import QObject

from model.modelserviceinterlayer import ModerlServiceInterlayer

class Model(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__interlayer = ModerlServiceInterlayer()
        
        self.__dates: list[str]

        self.__online_counts: list[int]
        self.__total_counts: list[int]
        self.__online_percents: list[int]

        self.inialize_data()

    def inialize_data(self):
        self.query_dates()
        self.query_date_online_counts_data(self.__dates)

    def query_dates(self):
        self.__dates = self.__interlayer.query_dates_from_db()

    def query_date_online_counts_data(self, date):
        data = self.__interlayer.query_date_online_counts(date[0])

        self.__online_counts = data["Online"]
        self.__total_counts = data["Total"]
        self.__online_percents = data["Percents"]



    '''
    Getters

    '''


    def get_dates(self):
        return self.__dates
    
    def get_online_counts(self):
        return self.__online_counts
    
    def get_total_counts(self):
        return self.__total_counts
    
    def get_online_percents(self):
        return self.__online_percents







