#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/21 


# 作用:对服务器批量执行命令，或者发送文件到其他机器
# 用法:
# 执行命令:python bat_exec.py DB uptime 或者 python bat_exec.py DB "ls | wc -l"
# 发送文件:
# python bat_exec.py DB pexpect-3.3.tar.gz /home/

# 配置文件的格式如下 下面例子前面的#需要去掉,配置好密码文件后，需要修改变量ip_list_file的值:
# [WEB]
# 192.168.56.102 root liu123
# [DB]
# 192.168.56.101 root liu123
# 192.168.56.102 root liu123

#
# 注意:如果发行版中没有pexpect模块 需要安装pexpect模块
# 警告:密码需要明文写进配置文件，可能不安全
#
import pexpect
import re
import sys


if __name__ == '__main__':
	pass
