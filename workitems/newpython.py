#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/13

import datetime
import os
import shutil
import zipfile

new = datetime.date.today()

spath = r'E:\upgrade\template'

dpath = r'E:\upgrade\%s' % new


def copy_dir():
    if not os.path.exists(dpath):
        shutil.copytree(spath, dpath)
        print 'Creating Success %s' % dpath
        return True
    else:
        print 'this  %s  is  exists' % dpath
        return False


def dump_table(tables):
    try:
        output = dpath + '\db_gamedata_update.sql'
        mysqlcmd = '''mysqldump  --lock-tables=false -h188.188.1.158 -uroot -plhb!@#$ aj2_gamedata_v2  {tables} t_identity_ver  > {output} '''.format(
            tables=tables, output=output)
        # print mysqlcmd
        os.system(mysqlcmd)
        os.chdir(dpath)
        zipname = 'db_gamedata_update.zip'
        f = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
        f.write('db_gamedata_update.sql')
        f.close()

    except Exception, e:
        print e
    finally:
        print os.path.dirname(output)


if __name__ == '__main__':
    pass
    # copy_dir()
    # global tables
    #
    # tables =str(raw_input('please input tables:\n'))
    # # tables = 't_panel'
    #
    # dump_table(tables)

import time
spath = r'E:\upgrade\template'


def outdir():
    dirs = time.strftime("%m%d", time.localtime())
    dpath = os.path.join(dirs)
    while True:

        if not os.path.exists(dpath):
            shutil.copytree(spath, dpath)
            break
        else:
            dpath = raw_input('please input direct:\n')
    return dpath



print outdir()
