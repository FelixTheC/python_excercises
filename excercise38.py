#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 16.06.19
@author: felix
"""

import os
import tarfile
import zipfile


class NoTarFile(Exception):
    pass


def test_tarfile(tmp_path):

    for index, letter in enumerate('abcde', 1):
        with open(f'{tmp_path}/{letter * index}.txt', 'w') as f:
            f.write(f'{letter * index}\n' * 100)

    tf = f'{tmp_path}/mytar.tar'
    with tarfile.open(tf, 'w') as t:
        for index, letter in enumerate('abcde', 1):
            t.add(f'{tmp_path}/{letter * index}.txt')

    return tf


def tar_to_zip(file, zippath=None):
    path = '/'.join(os.path.abspath(__file__).split('/')[:-1])
    if zippath is not None:
        path = zippath

    if not tarfile.is_tarfile(file):
        raise NoTarFile(f'{file} is not a tar archive')

    tar = tarfile.open(file)
    tar.extractall(f'/tmp/{tar.name}')
    tar.close()

    with zipfile.ZipFile(f'{tar.name.split(".")[0]}.zip', 'w', zipfile.ZIP_DEFLATED) as new_zip:
        os_walk = list(os.walk(f'/tmp/{tar.name}'))
        directory_list = os_walk[-1][0].split(tar.name)
        directory = directory_list[0][:-1] + directory_list[-1]
        new_zip.write(directory)
        for dirname, subdir, files in os_walk:
            for f_name in files:
                new_zip.write(os.path.join(dirname, f_name), f'{directory}/{f_name}')
    new_zip.close()


if __name__ == '__main__':
    tar_to_zip(test_tarfile('/'.join(os.path.abspath(__file__).split('/')[:-1])))
