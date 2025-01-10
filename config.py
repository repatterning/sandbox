"""config.py"""
import os
import datetime


class Config:
    """
    Config
    """

    def __init__(self) -> None:
        """
        Constructor<br>
        -----------<br>

        Variables denoting a path - including or excluding a filename - have an underscore suffix; this suffix is
        excluded for names such as warehouse, storage, depository, etc.<br><br>
        """

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')

        '''
        For configurations repository
        '''

        # Span
        self.starting = datetime.datetime.strptime('2022-01-01', '%Y-%m-%d')
        self.at_least = datetime.datetime.strptime('2025-01-05', '%Y-%m-%d')

        # Limits
        self.minimum = 5
        self.maximum = 7
