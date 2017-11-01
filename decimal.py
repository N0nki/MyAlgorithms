# coding: utf-8

"""
10進数→n進数変換
n進数→10進数変換
"""

from __future__ import print_function

def decimal2nary(decimal_num, base):
    """
    10進数→n進数変換
    """
    table = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = []
    
    if decimal_num == 0:
        result.append("0")
    else:
        while decimal_num > 0:
            result.append(table[decimal_num % base])
            decimal_num /= base
    return "".join(reversed(result))

def nary2decimal(n_ary, base):
    """
    n進数→10進数変換
    """
    table = '0123456789abcdefghijklmnopqrstuvwxyz'
    # each_digit = [[int(n_ary[i]), int(base), len(n_ary)-(i+1)] for i in range(len(n_ary))]
    each_digit = [[table.find(n_ary[i]), int(base), len(n_ary)-(i+1)] for i in range(len(n_ary))]
    return reduce(lambda x,y: x+y, map(lambda x: x[0]*(x[1]**x[2]), each_digit))

if __name__ == "__main__":
    print(decimal2nary(10, 2))
    print(decimal2nary(256, 2))
    print(decimal2nary(245602, 2))
    print(nary2decimal("1010110101000", 2))
    print(nary2decimal("aa", 16))
