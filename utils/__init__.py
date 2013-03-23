#!/usr/bin/env python
# coding=utf-8

from time import localtime, strftime


def current_time():
    # '2013-02-28 20:05:01'
    return strftime("%Y-%m-%d %H:%M:%S", localtime())
