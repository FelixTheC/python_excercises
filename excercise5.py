#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 19:58:54 2018

@author: felix
"""
import json
import requests
import pandas as pd
from myrange_exercise2 import timeit

gist_url = 'https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json?__s=jrbakyaxv67up2tcemtu&utm_source=drip&utm_medium=email&utm_campaign=WPE+September+2018+cohort&utm_content=%5BWeekly+Python+Exercise+S18%5D+Exercise+%235+%E2%80%94+Big+cities'
filename = 'cities.csv'
filename2 = 'cities2.csv'

@timeit
def cities_to_csv(url=gist_url, filename=filename):
    request = requests.get(url)
    with open(filename, 'w+') as file:
        for i in get_json_data(json.loads(request.content)):
            file.write(i)
    
def get_json_data(json_data):
    for data in json_data:
        yield f"{data['city']}\t{data['state']}\t{data['rank']}\t{data['population']}\n"
    
@timeit
def pandas_test(url=gist_url, filename=filename2):
    df = pd.read_json(gist_url, 'records')
    df.to_csv(filename, sep='\t')
    

if __name__ == '__main__':
    # 0.0006813950008816189
    cities_to_csv()
    # 0.0002489683363172743
    pandas_test()