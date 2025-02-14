"""Module main.py"""
import logging
import os
import sys


def main():
    """
    Entry Point

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('SANDBOX')

    # Data
    if reacquire:
        src.data.interface.Interface().exc()

    # Attributes
    if explore:
        src.attributes.interface.Interface().exc()

    # Algorithms
    src.algorithms.interface.Interface().exc()

    # Delete Cache Points
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d\n',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Activate graphics processing units
    os.environ['CUDA_VISIBLE_DEVICES']='0'

    # Modules
    import config
    import src.algorithms.interface
    import src.attributes.interface
    import src.data.interface
    import src.functions.cache
    import src.functions.directories

    # Reacquire, Explore
    reacquire: bool = False
    explore: bool = False

    # Set up
    if reacquire:
        configurations = config.Config()

        directories = src.functions.directories.Directories()
        directories.cleanup(path=configurations.warehouse)
        directories.create(path=configurations.series_)

    main()
