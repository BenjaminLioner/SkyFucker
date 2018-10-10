# _*_ coding: utf-8 _*_
__author__ = "Carl Benjamin"
__date__ = "2018/10/9 11:46"

import nmap

def generate_ip(ip):
    ip_fenjie = ip.split('.')
    A = int(ip_fenjie[0])
    B = int(ip_fenjie[1])
    C = int(ip_fenjie[2])
    D = int(ip_fenjie[3])
    D += 1

    if((D//255)==1):
        D = 0
        C+=1
        if((C//255)==1):
            C=0
            B+=1
            if((B//255)==1):
                B=0
                A+=1
                if((A//255)==1):
                    A=0
    new_ip = '.'.join([str(A), str(B), str(C), str(D)])
    return new_ip


def get_port(port):
    port += 1
    return port


class PortScanner():
    pass
