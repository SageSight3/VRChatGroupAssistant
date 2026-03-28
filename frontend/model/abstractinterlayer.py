from PySide6.QtCore import QObject

from abc import ABCMeta, ABC, abstractmethod
from collections.abc import Mapping
from typing import Any

'''
Creating an abstract interlayer class allows for 
us to ensure that all methods the model needs to function
are defined, while doing so in a way, that will allow us to
swap the concrete interlayer object in the model with other types of
concrete interlayers, if needed. For example, for when VRCGA switches
from using basic files for data storage to using a full fledged database.

By creating an abstract intlerlayer class, we help guarantee that the frontend
will still be able to function, even if the backend were to be completely 
swapped out, provided we change the concrete interlayer as well, since no matter
what, the concrete interlayer will be required to implement overrides of the abstract
interlayer's methods.

Be sure to decorate all overridden methods in the concrete interlayer with the @override
decorator, for clarity on which methods in it are required to be there by the model. The
@override decorator comes from the typing module

EDIT: Version of Python being used for VRCGA's frontend at present is Python 3.11.9, which
doesn't have @override decorator. Update in future, but for now, just comment which
methods are overrides

EDIT: Abstract methods that have yet to be implemented will only raise an error if they're called

'''

err_msg_base = "ModelServiceInterlayer: "

# Combine QObject's and ABC's metaclasses so Abstract Interlayer can inherit from both of them
# ABC - Abstract Base Class
class QObjectABCMeta(ABCMeta, QObject.__class__):
    pass

# AbstractInterlayer will inherit from QObject, since the interlayer
# may need to be able to receive or emit signals
class AbstractInterlayer(QObject, ABC, metaclass=QObjectABCMeta):

    def __init__(self, parent=None):
        super().__init__(parent)

    '''
    Database Queries

    '''

    @abstractmethod
    def query_days_from_db(self) -> list[Mapping[str, str]]:
        raise NotImplementedError(err_msg_base + "query_dates_from_db() not implemented")

    @abstractmethod
    def query_date_online_counts_data(self, date) -> list[Mapping[str, Any]]:
        raise NotImplementedError(err_msg_base + "query_date_online_counts() not implemented")

    '''
    Config and Status Queries

    '''

    '''
    Inbound Communications from VRCGA Service

    '''


    '''
    Oubound Communication to VRCGA Service

    '''