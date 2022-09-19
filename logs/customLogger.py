import logging


class LogGen:

    @staticmethod
    def logGen():
        logging.basicConfig(filename='./logs' + '/automation.log',
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%d/%m/%y  %I:%M:%S %p',
                            force=True
                            )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
