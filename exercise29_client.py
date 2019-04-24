#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.04.19
@author: felix
"""
from flask import Flask, request
import requests as r

app = Flask(__name__)


def pathname_to_picklename(s):
    return s.replace(b'/', b'-')


@app.route('/client')
def rescan():
    pathname = request.query_string.decode('utf8')
    path = 'http://localhost:5000/rescan?'
    url = path + pathname
    response = r.get(url)
    return response.json()


if __name__ == '__main__':
    app.run(host='localhost', port=5001)
