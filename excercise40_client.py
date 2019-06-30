#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 30.06.19
@author: felix
"""
import asyncio


async def my_client(host='127.0.0.1', port=9999):
    reader, writer = await asyncio.open_connection(host=host, port=port)
    for msg in ['say hello', 'sayworld', 'increment55', 'increment 40', 'stupid question', 'bye']:
        writer.write(msg.encode())
        data = await reader.read(1024)
        print(data.decode())

    writer.close()


def run_my_client():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_client())
    loop.close()


if __name__ == '__main__':
    run_my_client()
