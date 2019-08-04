#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 04.08.19
@author: felix
"""

import sys
import os
from time import strftime
from time import gmtime
import glob
from tinytag import TinyTag
import pandas as pd


def get_duration(dir: str, filename: str) -> float:
    tag = TinyTag.get(os.path.join(dir, filename))
    return tag.duration


def sec_to_min(seconds: float) -> float:
    return float(f'{seconds/60:.2f}')


def mp4_files_info(_dir: str, pattern='*.mp4'):
    files = glob.glob1(_dir, pattern)
    if not files:
        return f'No "{pattern.split(".")[-1]}" files found in {_dir}'
    df = pd.DataFrame(data={'filename': files})
    df['duration_sec'] = df['filename'].apply(lambda x: get_duration(_dir, x))
    df['duration_min'] = df['duration_sec'].apply(lambda x: sec_to_min(x))
    details = [f"{i.title()} time: {getattr(df['duration_min'], i)():.4f}" for i in ['min', 'max', 'mean', 'std']]
    details.append(f"Total time: {strftime('%H:%M', gmtime(df['duration_sec'].sum()))}")
    return '\n'.join(details)


if __name__ == '__main__':
    print(mp4_files_info(sys.argv[-1]))
