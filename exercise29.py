#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.04.19
@author: felix
"""
from flask import Flask, request
import os
import pickle
import json
from excercise26 import FileList

app = Flask(__name__)


def pathname_to_picklename(s):
    return s.replace(b'/', b'-')


@app.route("/scan")
def scan():
    pathname = request.query_string

    if not os.path.exists(pathname):
        return f"Error: No such path '{pathname}'"
    elif not os.path.isdir(pathname):
        return f"Error: '{pathname}' is not a directory"
    else:
        fl = FileList(pathname)
        pickle_filename = pathname_to_picklename(pathname)
        fl.scan()
        pickle.dump(fl, open(pickle_filename, 'wb'))
        return f"Successfully scanned and pickled."


@app.route('/rescan')
def rescan():
    pathname = request.query_string
    data = {}

    if not os.path.exists(pathname):
        data['error'] = f"No such path '{pathname}'"
    elif not os.path.isdir(pathname):
        data['error-'] = f"'{pathname}' is not a directory"
    elif not os.path.exists(pathname_to_picklename(pathname)):
        data['error-'] = f"No record of scanning '{pathname}'"
    else:
        fl = pickle.load(open(pathname_to_picklename(pathname), 'rb'))
        data = fl.rescan()
    for key, val in data.items():
        data[key] = list([i.decode('utf8') for i in val])

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run()
