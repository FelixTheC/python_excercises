#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 14.07.19
@author: felix
"""
import pickle
import socket

hostname = '127.0.0.1'


def send_client_message(s, message):
    s.send(message.encode())
    return pickle.loads(s.recv(1024))


def get_client_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.getfqdn(hostname)
    port = 9999
    s.connect((host, port))
    return s


def run_client():
    s = get_client_socket()

    for one_message in ['numbers',
                        'reverse_word hello',
                        'unicode_map exponentiation',
                        'this is garbage!']:

        print(f'Now sending {one_message}')
        response = send_client_message(s, one_message)
        print(f"Response: {response}")
        print(f"Response type: {type(response)}")
