#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 20:28:33 2019

@author: felix
"""
import os
import hashlib


def get_file_info(path):
    file_infos = []
    for root, dirs, files in os.walk(path, topdown=True):
        for file in files:
            pfile = os.path.join(root, file)
            file_info = dict()
            file_info['filename'] = file
            file_info['path'] = pfile
            file_info['timestamp'] = os.stat(pfile).st_mtime
            file_info['sha1'] = get_file_hash(pfile).hexdigest()
            file_infos.append(file_info)
    return file_infos


def get_file_hash(filename):
    file_hash = hashlib.sha1()
    contents = []
    with open(filename, 'r+') as file:
        contents = file.readlines()
    for content in contents:
        file_hash.update(content.encode('utf8'))
    return file_hash
