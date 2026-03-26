from collections.abc import Mapping

from model.abstractinterlayer import AbstractInterlayer

class ModerlServiceInterlayer(AbstractInterlayer):

    def __init__(self, parent=None):
        super().__init__(parent)

    '''
    Database Queries

    '''



    # Override
    def query_dates_from_db(self) -> list[str]:

        # TEST
        return list({
            "a_date",
            "another_date"
        })

    # Override
    def query_date_online_counts(self, date) -> Mapping[str, list[int]]:

        # TEST
        return {
            "Online": [1, 3, 2, 5],
            "Total": [4, 3, 4, 1],
            "Percents": [43, 13, 24, 53]
        }



    '''
    Config and Status Queries

    '''



    '''
    Inbound Communications from VRCGA Service

    '''



    '''
    Oubound Communication to VRCGA Service

    '''