#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 30.06.19
@author: felix
"""


import socket
import sys


def my_server(host='127.0.0.1', port=9999):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1024)
        conn, _ = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                msg = data.decode()
                if 'say' in msg.lower():
                    msg = msg.replace('say', '').strip()
                    conn.sendall(msg.encode())
                elif 'increment' in msg.lower():
                    msg = msg.replace('increment', '').strip()
                    msg = f'{int(msg) + 1}'
                    conn.sendall(msg.encode())
                elif 'bye' in msg.lower():
                    conn.sendall(b'bye')
                    break
                else:
                    conn.sendall(b"I don't understand.")
        s.close()


if __name__ == '__main__':
    try:
        my_server()
    except KeyboardInterrupt:
        sys.stdout.write('bye bye')
