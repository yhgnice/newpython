#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/29 

import os
import time


def pathdir(dpath):
	dirpath = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime())
	backdir = os.path.join(dpath, dirpath)
	print backdir
	if not os.path.exists(backdir):
		os.mkdir(backdir)

	return backdir

def backup_db(pathdir, dblist):
	try:
		for db in dblist:
			cmd = 'mysqldump   --lock-tables=false  -h188.188.1.158 -uroot -plhb!@#$  {db}  >  {pathdir}/{db}.sql '.format(db=db,
			                                                                                        pathdir=pathdir)
			os.system(cmd)

	except Exception, e:
		print e


if __name__ == '__main__':
	dpath = r'c:\abcd\backup'


	dblist = ['aj2_account_0','aj2_account_9501', 'aj2_account_across',
	          'aj2_account_green', 'aj2_account_green_across', 'aj2_account_korea',
	          'aj2_account_malai', 'aj2_account_malai_across', 'aj2_account_qq',
	          'aj2_account_qq_across', 'aj2_account_shouyou', 'aj2_account_taiguo',
	          'aj2_account_taiguo_across', 'aj2_account_taiwan', 'aj2_account_taiwan_across',
	          'aj2_account_u3d', 'aj2_account_v2', 'aj2_account_yuenan',
	          'aj2_account_yuenan_across', 'aj2_account_yuenan_banshu',
	          'aj2_active_code', 'aj2_active_code_korea', 'aj2_backadmin',
	          'aj2_backadmin_korea', 'aj2_game_config', 'aj2_game_config_shouyou',
	          'aj2_gamedata_0', 'aj2_gamedata_2', 'aj2_gamedata_9501',
	          'aj2_gamedata_green', 'aj2_gamedata_korea', 'aj2_gamedata_malai',
	          'aj2_gamedata_qq', 'aj2_gamedata_shouyou', 'aj2_gamedata_taiguo',
	          'aj2_gamedata_taiwan', 'aj2_gamedata_u3d', 'aj2_gamedata_v2',
	          'aj2_gamedata_yuenan', 'aj2_gamedata_yuenan_across',
	          'aj2_gamedata_yuenan_banshu', 'aj2_gateway', 'aj2_gateway_qq',
	          'aj2_msg_shouyou', 'aj2_msg_shouyou_new', 'aj2_role_0',
	          'aj2_role_9501', 'aj2_role_across', 'aj2_role_across_9501',
	          'aj2_role_green', 'aj2_role_green_across', 'aj2_role_korea',
	          'aj2_role_malai', 'aj2_role_malai_across', 'aj2_role_qq',
	          'aj2_role_qq_across', 'aj2_role_shouyou', 'aj2_role_taiguo',
	          'aj2_role_taiguo_across', 'aj2_role_taiwan', 'aj2_role_taiwan_across',
	          'aj2_role_v2_1', 'aj2_role_yuenan', 'aj2_role_yuenan_across',
	          'aj2_role_yuenan_banshu', 'aj2sy_msg', 'aj2sy_msg_new',
	          'ajsy_account', 'ajsy_gamedata', 'ajsy_role', 'data_editor',
	          'data_editor_publish', 'dzsf_msg', 'fs2_account',
	          'fs2_account_9501', 'fs2_account_across', 'fs2_account_banshu',
	          'fs2_game_config', 'fs2_gamedata', 'fs2_gamedata_banshu',
	          'fs2_role', 'fs2_role_9501', 'fs2_role_across',
	          'fs2_role_banshu', 'korea_account_9501', 'korea_role_9501',
	          'mysql', 'z_editor']
	newpath = pathdir(dpath)
	backup_db(pathdir=newpath, dblist=dblist)
