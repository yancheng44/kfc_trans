#!/usr/bin/env python
#coding=utf-8

import logging
import logging.handlers

class mylogger(object):
    def __init__(self, logger):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        handler = logging.handlers.TimedRotatingFileHandler("trans.log", 'D')
        fmt = logging.Formatter(
            "%(asctime)s - %(parameter)s - %(filename)s - %(function)s - %(lineno)s - %(levelname)s - %(message)s")
        handler.setFormatter(fmt)
        logger.addHandler(handler)

    def getlog(self):
        return self.logger


