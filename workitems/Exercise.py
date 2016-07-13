#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/13
from multiprocessing import Pool

import time

def f(x):
    time.sleep(1)
    return x*x


if __name__ == '__main__':
    p = Pool(100)
    print p.map(f,range(100))
    print 'test'