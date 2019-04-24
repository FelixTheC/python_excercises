#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: felix
"""
import pickle
import os
import hashlib


class FileInfo(object):

    def __init__(self, filename, mtime, sha1):
        self.filename = filename
        self.mtime = mtime
        self.sha1 = sha1

    def __eq__(self, other):
        try:
            return self.sha1 == other.sha1
        except AttributeError:
            pass

    def __str__(self):
        return f'FileInfo for {self.filename}, mtime {self.mtime}, sha1 {self.sha1}'

    def __repr__(self):
        return f'{self.filename}'

    def __hash__(self):
        return hash(f'{self.sha1}')


class FileList(object):
    save_file_name = 'file_infos.pickle'
    file_infos = []

    def __init__(self, filepath):
        self.filepath = filepath

    def scan(self, join=True):
        tmp_list = []
        for root, dirs, files in os.walk(self.filepath, topdown=True):
            for file in files:
                tmp_file = os.path.join(root, file)
                try:
                    file_hash = hashlib.sha1(open(tmp_file, 'rb').read()).hexdigest()
                except (PermissionError, MemoryError):
                    file_hash = '0'
                tmp_list.append(FileInfo(tmp_file,
                                         os.stat(tmp_file).st_mtime,
                                         file_hash
                                         ))
        if join is True:
            self.file_infos = tmp_list
        else:
            return tmp_list

    def rescan(self):
        scan_dict = {'added': [], 'removed': [], 'changed': [], 'unchanged': []}
        scanned = self.scan(False)
        changed = self.check_changes(self.file_infos, scanned)
        scan_dict['added'] = list([i.filename for i in scanned if i not in self.file_infos])
        scan_dict['removed'] = list([i.filename for i in self.file_infos if i not in scanned])
        scan_dict['unchanged'] = list([i.filename for i in self.file_infos if i not in changed])
        scan_dict['changed'] = list([i.filename for i in changed])
        return scan_dict

    def check_changes(self, origin, other):
        ori = {i.filename: i for i in origin}
        oth = {i.filename: i for i in other}
        changed_files = []
        for key, val in ori.items():
            if key in oth:
                if val.sha1 != oth[key].sha1:
                    changed_files.append(val)
        return changed_files

    @property
    def all_file_infos(self):
        return self.file_infos

    def save(self):
        file = open(self.save_file_name, 'wb')
        pickle.dump(self.file_infos, file, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self):
        file = open(self.save_file_name, 'rb')
        self.file_infos = pickle.load(file)
