#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:42:40 2018

@author: felix
"""

import re
import datetime
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        rf = func(*args, **kwargs)
        print((time.time() - start_time) * 3600)
        return rf
    return wrapper
        

class LogDicts():
    
    _filename = None
    _logdic_array = None
    _ip_addr = re.compile(r'[0-9.]{12,17}')
    _timestmp = re.compile(r'\[(.+?)\]')
    _req = re.compile(r'\"(.+?)\"')
    
    def __init__(self, file, old=True):
        try:
            self._filename = file
            self._logdic_array = []
            if old:
                self._create_logdic_array()
            else:
                self._create_logdic_array_v2()
        except TypeError:
            raise TypeError('Must be of type str')
            
    def __str__(self):
        return f'LogDicts object for {self._filename}'
    
    def __repr__(self):
        return f'LogDicts object for {self._filename}'
            
    def dicts(self, key=None):
        if key is not None:
            return sorted(self._logdic_array, key=key)
        else:
            return self._logdic_array
    
    def iterdicts(self, key=None):
        if key is not None:
            yield from sorted(self._logdic_array, key=key)
        else:
            yield from self._logdic_array
            
    def earliest(self):
        try:
            return min(self._logdic_array, key=lambda x: x['timestamp'])
        except TypeError:
            return None
    
    def latest(self):
        try:
            return max(self.__logdic_array, key=lambda x: x['timestamp'])
        except TypeError:
            return None
    
    def for_ip(self, ip_address, key=None):
        filtered_ip = list([x for x in self.__logdic_array if x['ip_address'] == ip_address])
        if key is not None:
            return sorted(filtered_ip, key=key)
        else:
            return filtered_ip
    
    def for_request(self, text, key=None):
        filtered_request = list([x for x in self.__logdic_array if x['request'] == text])
        if key is not None:
            return sorted(filtered_request, key=key)
        else:
            return filtered_request
    
    @timeit
    def _create_logdic_array(self):
        # slower function
        if self._logdic_array is None:
            self._logdic_array = []
        with open(self._filename, 'r') as file:
            for line in file.readlines():
                logdict = {}
                logdict['ip_address'] = self._ip_addr.findall(line)[0]
                logdict['timestamp'] = self._str_to_time(self._timestmp.findall(line)[0].replace('[', '').replace(']', ''))
                logdict['request'] = self._req.findall(line)[0]
                self._logdic_array.append(logdict)
           
    @timeit
    def _create_logdic_array_v2(self):
        # faster function
        if self._logdic_array is None:
            self._logdic_array = []
        with open(self._filename, 'r') as file:
            for line in file.readlines():
                self._logdic_array.append(self.line_to_dict(line))
                
    def line_to_dict(self, line):
        ip_address = line.split()[0]
        
        timestamp_start = line.index('[') + 1
        timestamp_end = line.index(']')
        timestamp = line[timestamp_start:timestamp_end]
        
        request_start = line.index('"') + 1
        request_end = line[request_start:].index('"')
        request = line[request_start:request_start+request_end]
        
        return {'ip_address': ip_address,
                'timestamp': timestamp,
                'request': request}
    
    def _str_to_time(self, timestring):
        new_time = datetime.datetime.strptime(timestring, '%d/%b/%Y:%H:%M:%S %z')
        return new_time.strftime('%Y-%m-%d %H:%M:%S %z')
    
    
if __name__ == '__main__':
    log = LogDicts('mini-access-log.txt')
    log2 = LogDicts('mini-access-log.txt', old=False)
    