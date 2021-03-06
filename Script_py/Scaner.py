# -*- coding:utf8 -*-
import socket
import time
import _thread
import os
from time import sleep

socket.setdefaulttimeout(1)

def socket_port(ip, port):
    try:
        if port >= 65535:
            return
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            lock.acquire()
            print(ip, u':', port, u'端口开放')
            lock.release()
        s.close()
    except Exception as e:
        pass

def ip_scan(ip):
    """
    输入IP，扫描IP的0-65534端口情况
    """
    try:
        print(u'开始扫描 %s' % ip)
        start_time = time.time()
        for j in range(0, 660):
            for i in range(j * 100, 100 * (j + 1)):
                #print(i)
                _thread.start_new_thread(socket_port, (ip, int(i)))
            sleep(0.2)  # 休眠 防止线程创建的过多报错（can not create new start thread）
        print('扫描端口完成，总共用时 ：%.2f' % (time.time() - start_time))
    except Exception as e:
        print('扫描ip出错',e)

if __name__ == '__main__':
    lock = _thread.allocate_lock()
    ipadd = ['192.168.0.1','192.168.0.2']
    for ip in ipadd:
        ip_scan(ip)
        #print(ip)
