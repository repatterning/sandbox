import glob
import logging
import os

import config


class Points:

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

    def __get_listings(self) -> list:
        """

        :return:
        """

        listings = glob.glob(pathname=os.path.join(self.__configurations.series_, '**', '*.csv'), recursive=True)

        return listings

    def exc(self) -> list:
        """

        :return: A list of data file names.
        """

        listings = self.__get_listings()
        logging.info(listings)

        return listings
