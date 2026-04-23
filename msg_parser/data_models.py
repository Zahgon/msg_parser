# coding=utf-8
from datetime import datetime
from datetime import timedelta
from struct import unpack

from .properties import DATA_TYPE_MAP


class DataModel(object):
    def __init__(self):
        self.data_type_name = None

    @staticmethod
    def lookup_data_type_name(data_type):
        pass

    def get_value(self, data_value, data_type_name=None, data_type=None):

        pass

    @staticmethod
    def PtypUnspecified(data_value):
        pass

    @staticmethod
    def PtypNull(_):
        pass

    @staticmethod
    def PtypInteger16(data_value):
        pass

    @staticmethod
    def PtypInteger32(data_value):
        pass

    @staticmethod
    def PtypFloating32(data_value):
        pass

    @staticmethod
    def PtypFloating64(data_value):
        pass

    @staticmethod
    def PtypCurrency(data_value):
        pass

    @staticmethod
    def PtypFloatingTime(data_value):
        pass

    @staticmethod
    def PtypErrorCode(data_value):
        pass

    @staticmethod
    def PtypBoolean(data_value):
        pass

    @staticmethod
    def PtypObject(data_value):
        pass

    @staticmethod
    def PtypInteger64(data_value):
        pass

    @staticmethod
    def PtypString8(data_value):
        pass

    @staticmethod
    def PtypString(data_value):
        pass

    @staticmethod
    def PtypTime(data_value):
        pass

    @staticmethod
    def PtypGuid(data_value):
        pass

    @staticmethod
    def PtypServerId(data_value):
        pass

    @staticmethod
    def PtypRestriction(data_value):
        pass

    @staticmethod
    def PtypRuleAction(data_value):
        pass

    @staticmethod
    def PtypBinary(data_value):
        pass

    @staticmethod
    def PtypMultipleInteger16(data_value):
        pass

    @staticmethod
    def PtypMultipleInteger32(data_value):
        pass

    @staticmethod
    def PtypMultipleFloating32(data_value):
        pass

    @staticmethod
    def PtypMultipleFloating64(data_value):
        pass

    @staticmethod
    def PtypMultipleCurrency(data_value):
        pass

    @staticmethod
    def PtypMultipleFloatingTime(data_value):
        pass

    @staticmethod
    def PtypMultipleInteger64(data_value):
        pass

    @staticmethod
    def PtypMultipleString(data_value):
        pass
        # string_list = []
        # for item_bytes in data_value:
        #     if item_bytes and '\x00' in item_bytes:
        #         item_bytes = item_bytes.replace('\x00', '')
        #     string_list.append(item_bytes.decode('utf-16-le'))
        # return string_list

    @staticmethod
    def PtypMultipleString8(data_value):
        pass

    @staticmethod
    def PtypMultipleTime(data_value):
        pass

    @staticmethod
    def PtypMultipleGuid(data_value):
        pass

    @staticmethod
    def PtypMultipleBinary(data_value):
        pass


def get_floating_time(data_value):
    pass


def get_time(data_value):
    pass


def get_multi_value_offsets(data_value):
    pass
