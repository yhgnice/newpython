#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/15


from multiprocessing import Pool,Queue,Process
import os, time, random

'''

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(10)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()

    print 'All subprocesses done.'


# 写数据进程执行的代码:
def write(q):
    for value in range(1,10000):
    # for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

import time, threading

# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        # time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name

'''


from multiprocessing import Process

def f(name, Blog='www.google.com'):
    print  "hello", name
    print  "Blog:", Blog

if __name__ == '__main__':
    start=time.time()
    p = Pool()
    for i in range(30000):
        p.apply(f, args=("The_Third_Wave",))
    p.close()
    p.join()
    end=time.time()
    print 'Task  runs %0.2f seconds.' % ((end - start))