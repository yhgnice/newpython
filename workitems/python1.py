#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/12 

import re
import requests
from bs4 import BeautifulSoup



url = 'http://www.qy7788.com.cn/shiyongxinxi/shiyongxinxi193.html'

webcontext = requests.get(url).text

regex= re.compile('<div class="carea">(.+?)</div>',re.S)

urlregex = re.compile(r'<a href="(http://www.qy7788.com.cn/.+?/)\">(.+?)</a>',re.S)

for line in re.findall(urlregex,webcontext):
    print line[0],'\t' * 10,line[1]


# print re.findall(regex,webcontext)
# soup = BeautifulSoup(webcontext,'lxml')
# print soup.find_all('a')



import random

guest_list = ['石头','剪刀','布']
guize = [['布','石头'],['剪刀','布'],['石头','剪刀']]


while True:
    computer = random.choice(guest_list)
    print computer
    people = raw_input('请输入"石头","剪刀","布":\n').strip()
    if people not in guest_list:
        people = raw_input('请输入"石头","剪刀","布":\n').strip()
        continue



    if computer == people:
        print  '0 vs 0'
    elif [computer,people] in guize:
        print '电脑胜利'
    else:
        print 'people 胜利'
        break


if __name__ == '__main__':
    pass

