#!/usr/bin/env python
# -*- coding: gbk -*-
# @Time    : 2016/7/7 21:04
# @Site    : http://www.google.com
# @Software: PyCharm

from struct import *
import os
os.chdir(r'C:\new_tdx\vipdoc\sz\lday')
filepath=r'sz000680.day'
ofile=open(filepath,'rb')
buf=ofile.read()
ofile.close()

ifile=open('sz000680.txt','w')
num=len(buf)
no=num/32
b=0
e=32
line=''

for i in xrange(no):
   a=unpack('IIIIIfII',buf[b:e])
   line=str(a[0])+' '+str(a[1]/100.0)+' '+str(a[2]/100.0)+' '+str(a[3]/100.0)+' '+str(a[4]/100.0)+' '+str(a[5]/10.0)+' '+str(a[6])+' '+str(a[7])+' '+'\n'
   print line
   ifile.write(line)
   b=b+32
   e=e+32
ifile.close()



if __name__ == '__main__':
    pass