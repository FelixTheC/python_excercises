#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.09.19
@author: felix
"""

import cmd
from typing import List


ops = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}


def val_to_pos_int(arg: any) -> int:
    try:
        val = int(arg)
    except (AttributeError, ValueError, TypeError):
        return 0
    else:
        return val if val >= 0 else 0


def get_val_list(arg: str) -> List[int]:
    return list([j for j in [val_to_pos_int(i) for i in arg.split(" ")] if j > 0])


def calculation(base: int, args: List[int], method: str) -> int:
    if len(args) == 1:
        return getattr(int, f'__{method}__')(base, args[0])
    else:
        return calculation(getattr(int, f'__{method}__')(base, args.pop()), args, method)


def operation(args: List[int], method: str, erro_msg: str) -> int or str:
    try:
        base = args[0]
        op_args = args[1:]
        if not op_args:
            return base
        else:
            return calculation(base, op_args, method)
    except (IndexError, ZeroDivisionError):
        return erro_msg


class Menu(cmd.Cmd):
    prompt = '(calculator) '

    def do_add(self, arg: str) -> None:
        summands = get_val_list(arg)
        print(f'{operation(summands, "add", "Nothing to add")}')

    def do_sub(self, arg: str) -> None:
        subtracts = get_val_list(arg)
        print(f'{operation(subtracts, "sub", "Nothing to subtract")}')

    def do_mul(self, arg: str) -> None:
        multi = get_val_list(arg)
        print(f'{operation(multi, "mul", "Nothing to multiply")}')

    def do_div(self, arg: str) -> None:
        dividends = get_val_list(arg)
        print(f'{operation(dividends, "truediv", "Nothing to divide")}')

    def do_EOF(self, arg: str) -> bool:
        return True
    
    def precmd(self, line):
        if line[0] in ops.keys():
            line = line.replace(line[0], ops[line[0]])
        return super(Menu, self).precmd(line)


if __name__ == '__main__':
    Menu().cmdloop()
