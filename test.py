#!/usr/bin/env python
#coding=utf-8


from logger import logging


def test():
    if True:
        logging.info("test")
    else:
        logging.error("wront")

if __name__ == '__main__':
    test()



