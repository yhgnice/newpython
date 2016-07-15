#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/14 

file = r'E:\upgrade\2016-07-14\cachelist.html'


import re

pt = re.compile('td>(.+?)</td>            <td align="left">(.+?)</td>',re.S)

def write_sql(info):
    with open('update.sql','a') as sql_write:
        sql_write.write(info)
        sql_write.write('\n')


with open(file) as fs:
    rest = pt.findall(fs.read().decode('gbk'))
    strf = str(raw_input('please input search:'))
    for line in rest:
        # print line[1]
        if re.findall(strf,line[1],re.I):
            print line[1]
    # for line in rest:
    #     if strf in line[1]:
    #         print line[0],line[1]
    #         write_sql(line[1])






if __name__ == '__main__':
    pass




