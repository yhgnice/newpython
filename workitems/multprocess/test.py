#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/15 


import multiprocessing
import time

def worker_1(interval):
    print "worker_1"
    time.sleep(interval)
    print "end worker_1"

def worker_2(interval):
    print "worker_2"
    time.sleep(interval)
    print "end worker_2"

def worker_3(interval):
    print "worker_3"
    time.sleep(interval)
    print "end worker_3"



class clock_process(multiprocessing.Process):
    def __init__(self,interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval


    def run(self):
        n = 5
        while n > 0:
            print 'the time is {0}'.format(time.ctime())
            time.sleep(self.interval)
            n-=1







if __name__ == "__main__":
    '''
    p1 = multiprocessing.Process(target = worker_1, args = (2,))
    p2 = multiprocessing.Process(target = worker_2, args = (3,))
    p3 = multiprocessing.Process(target = worker_3, args = (4,))

    p = clock_process(3)
    p.start()
    # p1.start()
    # p2.start()
    # p3.start()
    '''
