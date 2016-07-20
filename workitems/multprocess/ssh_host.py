#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by   2016/07/15 

import paramiko
from multiprocessing import Process, Pool
import time
import threading
import re



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
    except Exception, e:
        reseult['err'] = e
    finally:
        # return reseult
        '''
        1.output
        print host, "\t",
        err_len = stderr.read()
        if len(err_len) > 0:
            print err_len
        print stdout.read()
        '''
        print  reseult.get('host'), "\t", reseult.get('stderr'), reseult.get('stdout'), '\n',
        res  = re.findall('INFO: Server startup in',reseult)
        if res:
            print 'OK'
        ssh.close()


def main(hostfile):
    start = time.time()
    with open(hostfile) as fe:
        for line in fe.readlines():
            sid = line.split()[0]
            host_ip = line.split()[1]
            newcmd = cmd.replace("lhbsid", sid)
            a = threading.Thread(target=ssh_host_paramiko, name='ssh_processlist',
                                 args=(host_ip, user, key_path, port, newcmd,))
            a.start()
        a.join()
        end = time.time()
        print 'Task  runs %0.2f seconds.' % ((end - start))


if __name__ == '__main__':
    user = 'root'
    key_path = r'D:\Sessions\key\Identity_aj2'
    port = 59878
    cmd = str(raw_input('Please input your cammand:\n'))
    hostfile = r'c:\yhglist'

    res = raw_input('确定是否继续执行，y or n:\n').upper()

    if res == 'Y':
        main(hostfile)
    print 'Bye,bye...'
    '''

    p = Pool(300)
    with open(hostfile) as fe:
        for line in fe.readlines():

            host_ip = line.split()[1]

            p.apply_async(ssh_host_paramiko, args=(host_ip,user,key_path,port,cmd,))


    p.close()
    p.join()

    '''

































