#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/13

import time
import os
import shutil
import zipfile
import re
import webbrowser

spath = r'E:\upgrade\template'

cachelist = os.path.join(spath,'cachelist.html')


def outdir():
    try:
        dirs = time.strftime("%m%d", time.localtime()) + str('01')
        dpath = os.path.join('E:\upgrade', dirs)
        while True:

            if not os.path.exists(dpath):
                shutil.copytree(spath, dpath)
                # os.mkdir(dpath)
                break
            else:
                print '%s,目录已存在' % dpath
                newdir = (raw_input('please input direct:\n'))
                dpath = os.path.join('E:\upgrade', newdir)
        return dpath
    except Exception,e:
        print e


dpath = os.path.join('E:\upgrade',outdir())

def dump_table(tables):
    try:
        output = dpath + '\db_gamedata_update.sql'
        mysqlcmd = '''mysqldump  --lock-tables=false -h188.188.1.158 -uroot -plhb!@#$ aj2_gamedata_v2  {tables} t_identity_ver  > {output} '''.format(
            tables=tables, output=output)
        os.system(mysqlcmd)
        os.chdir(dpath)
        batfile = 'echo {mysqlcmd} > sql.bat '.format(mysqlcmd=mysqlcmd)
        os.system(batfile)

        zipname = 'db_gamedata_update.zip'
        f = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
        f.write('db_gamedata_update.sql')
        f.close()

    except Exception, e:
        print e
    finally:
        print os.path.dirname(output)


def write_sql(info):
    outsql=os.path.join(dpath,'update.sql')
    with open(outsql, 'a') as sql_write:
        sql_write.write(info)
        sql_write.write('\n')


def html_re(searhstr):
    pt = re.compile('td>(.+?)</td>            <td align="left">(.+?)</td>', re.S)

    with open(cachelist) as fs:
        rest = pt.findall(fs.read().decode('gbk'))
        # strf = str(raw_input('please input search:'))
        for line in rest:
            if re.findall(searhstr, line[1], re.I):
                print line[0], line[1]
                write_sql(line[1])


def updata_sql(tables):
    for tab in tables.split():
        res1 = re.sub('t_', '', tab)
        searhstr = re.sub('_', '', res1)
        print searhstr
        if 'xsactivityitemreal' == searhstr:
            html_re('xsactvityrewarditemReal')
        html_re(searhstr)


def main(tables):

    dump_table(tables)
    updata_sql(tables)
    webbrowser.open_new(cachelist)

if __name__ == '__main__':
    # tables = 't_panel'
    tables =str(raw_input('please input tables:\n'))
    main(tables)

