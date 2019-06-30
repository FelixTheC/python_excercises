#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 16.06.19
@author: Reuven M. Lerner
"""

import pytest
import tarfile
import zipfile

from excercise38 import tar_to_zip


@pytest.fixture
def test_tarfile(tmp_path):

    for index, letter in enumerate('abcde', 1):
        with open(tmp_path / f'{letter * index}.txt', 'w') as f:
            f.write(f'{letter * index}\n' * 100)

    tf = tmp_path / 'mytar.tar'
    with tarfile.open(tf, 'w') as t:
        for index, letter in enumerate('abcde', 1):
            t.add(tmp_path / f'{letter * index}.txt')

    return tf


def test_tar_to_zip(tmp_path, test_tarfile):
    tar_to_zip(test_tarfile, zippath=tmp_path)

    assert len(list(tmp_path.glob('*.zip'))) == 1

    zf = zipfile.ZipFile(tmp_path / 'output.zip')
    zf.extractall(path=tmp_path)
    assert len(list(tmp_path.glob('*.txt'))) == 5
