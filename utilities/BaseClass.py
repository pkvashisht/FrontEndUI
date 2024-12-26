import inspect
import logging

import pytest
@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('/Users/pkvas/FrontEndUI/TestLogs/logfile.log')
        formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
        fileHandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger