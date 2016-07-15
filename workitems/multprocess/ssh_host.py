#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/15 

import paramiko


def ssh_host_paramiko(host,user,key_path,port,cmd,password=None):
    reseult = {}
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    key_filename=paramiko.DSSKey.from_private_key_file(key_path)
    ssh.connect(host,port,user,password,key_filename)
    stdin,stdout,stderr = ssh.exec_command('echo abcd test')

    reseult['host'] = host
    reseult['stdout'] = stdout.read()
    reseult['stderr'] = stderr.read()
    # cmd_result = stdout.read(),stderr.read()
    # for line in cmd_result:
    #     print line
    return reseult
    ssh.close()


def Sshconnect(host,user,id,cmd):
    try:
        paramiko.util.log_to_file('/tmp/yhglogin.log')
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        privatekey = os.path.expanduser('/root/shell/Identity_aj2')
        key = paramiko.DSSKey.from_private_key_file(privatekey)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host,port=59878,username=user,pkey=key)
        for command in cmd:
            stdin,stdout,stderr = ssh.exec_command(command,timeout=3)
            print '%s\n' % host,stdout.read(),stderr.read()
        print '--' *  60
        ssh.close()
    except:
        print '%s\tError\n' %(host)


host='61.160.242.95'
user='root'
key_path=r'D:\Sessions\key\Identity_aj2'
port=59878
cmd = 'echo abcd'

print ssh_host_paramiko(host,user,key_path,port,cmd)


if __name__ == '__main__':
    pass