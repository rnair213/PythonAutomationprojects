import logging
from time import asctime


class Logger:
    def __init__(self, logger, file_leve= logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        logging.basicConfig(filename="logfile.log", filemode='w', format='%(asctime)s: %(levelname)s: %(message)s'
                            , level=logging.INFO)


