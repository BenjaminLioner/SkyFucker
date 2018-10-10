# _*_ coding: utf-8 _*_
__author__ = "Carl Benjamin"
__date__ = "2018/10/9 19:50"
import nmap

host  = '101.37.225.65'
nm = nmap.PortScanner()
result = nm.scan(host)
print(result)
