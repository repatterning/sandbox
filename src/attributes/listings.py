"""Module listings.py"""
import glob
import os

import config


class Listings:
    """
    Listings
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

    def __of_timeseries_directories(self) -> list:
        """
        Gets the time series directories

        :return:
        """

        listings = glob.glob(pathname=os.path.join(self.__configurations.series_, '**', '**'))

        return listings

    def exc(self) -> list:
        """

        :return: A list of data file names.
        """

        listings = self.__of_timeseries_directories()

        return listings
