#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.07.19
@author: felix
"""
from importlib import import_module
import socket
import os
import pickle
from typing import List, Dict

hostname = '127.0.0.1'


def get_client_connection() -> socket:
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    host = socket.getfqdn(hostname)
    port = 9999
    serversocket.bind((host, port))

    serversocket.listen()
    print("Ready to accept connection")

    clientsocket, addr = serversocket.accept()
    return clientsocket


def find_function_files() -> List[str]:
    path, base, files, _ = list(os.fwalk())[0]
    server_funcs = [i for i in files if i[:len('server_func')] == 'server_func']
    return server_funcs


def create_function_dict(server_funcs: List[str]) -> Dict[str, str]:
    actions = {}
    base_dir = os.path.basename(os.path.dirname(__file__))
    for sv in server_funcs:
        module = import_module(f'{base_dir}.{sv.replace(".py", "")}')
        tmp = {i: getattr(module, i) for i in dir(module) if callable(getattr(module, i))}
        actions = {**actions, **tmp}
    return actions


def run_server() -> None:
    clientsocket = get_client_connection()
    actions = create_function_dict(find_function_files())

    while True:
        client_message = clientsocket.recv(1024).decode()

        if not client_message:
            break

        print(f"Received: '{client_message}'")

        command, *args = client_message.split()
        if command == 'bye':
            break
        elif command not in actions:
            clientsocket.send(pickle.dumps(f"Unknown command '{client_message}'"))
        else:
            try:
                result = actions[command](*args)
                clientsocket.send(pickle.dumps(result))
            except Exception as e:
                clientsocket.send(pickle.dumps(f"Error for '{client_message}' - {e} "))

    clientsocket.close()


if __name__ == '__main__':
    funcs = create_function_dict(find_function_files())
