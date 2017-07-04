import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler


class Mylogger(object):
    def __init__(self):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        handler = logging.handlers.TimedRotatingFileHandler("trans.log", 'D')
        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(fmt)
        self.logger.addHandler(handler)

    def getlog(self):
        return self.logger

logging = Mylogger().getlog()

if __name__ == '__main__':
    mylogger = Mylogger()
    log = mylogger.getlog()
    log.info("test444")


