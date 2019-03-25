#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 20:43:40 2018

@author: felix
"""
import re

def logtolist(filename='mini-access-log.txt'):
    loglist = []
    ip_addr = re.compile(r'[0-9.]{12,17}')
    timestmp = re.compile(r'\[(.+?)\]')
    req = re.compile(r'\"(.+?)\"')
    with open(filename, 'r') as file:
        for line in file.readlines():
            logdict = {}
            logdict['ip_address'] = ip_addr.findall(line)[0]
            logdict['timestamp'] = timestmp.findall(line)[0].replace('[', '').replace(']', '')
            logdict['request'] = req.findall(line)[0]
            loglist.append(logdict)
    return loglist


if __name__ == '__main__':
    print(logtolist()[0]['ip_address'])