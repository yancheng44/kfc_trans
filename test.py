#!/usr/bin/env python
#coding=utf-8
import datetime

from logger import logging


def test():
    if True:
        logging.info("test")
    else:
        logging.error("wront")

FILENAME = "black"+datetime.datetime.now().strftime('%Y%m%d')
if __name__ == '__main__':
    print "%s" %FILENAME


