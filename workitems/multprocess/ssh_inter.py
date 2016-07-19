#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/15 

import paramiko

def ssh_host_paramiko(host, user, key_path, port, cmd, password=None):
    reseult = {}
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key_filename = paramiko.DSSKey.from_private_key_file(key_path)
        ssh.connect(host, port, user, password, key_filename)

        stdin, stdout, stderr = ssh.exec_command(cmd)


        reseult['host'] = host
        reseult['stdout'] = stdout.read()
        reseult['stderr'] = stderr.read()
        # cmd_result = stdout.read(),stderr.read()
        # for line in cmd_result:
        #     print line

    except Exception, e:
        reseult['err'] = e
    finally:
        return reseult
        ssh.close()


if __name__ == '__main__':
    host = '61.160.242.95'
    user = 'root'
    key_path = r'D:\Sessions\key\Identity_aj2'
    port = 59878
    cmd = 'ifconfig eth0 '
    new = ssh_host_paramiko(host, user, key_path, port, cmd)
    print new['stdout']
