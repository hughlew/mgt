# -*- coding: cp936 -*-
import os,sys,re,datetime

def lastline():
    global pos
    
    while True:
        pos = pos - 1
        try:
            f.seek(pos, 2) 
            if f.read(1) == '\n':
                break
        except:
            f.seek(0, 0)        
            return f.readline().strip()
    return f.readline().strip()  


if __name__ == "__main__":

    today = datetime.date.today()
    f = open('D:\Office\Script\Check Logfile\%s%s%s.log' %(today.year,today.month,today.day),'rb')
    pos = 0   
    for line in range(10):
        a= lastline()
        net = a.split(' ')
        if net[-1] == 'kb/s':
            print net[-2]
            break
    f.close()
