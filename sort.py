# coding: utf-8

"""
ソートアルゴリズム
* バブルソート
* 挿入ソート
* 選択ソート
* ヒープソート
"""

from __future__ import division

def bubble_sort(l):
    """バブルソート"""
    _l = l[:]
    sorted_pos = len(l) - 1

    for n in range(sorted_pos):
        for idx in range(sorted_pos - n):
            if _l[idx] > _l[idx+1]:
                _l[idx], _l[idx+1] = _l[idx+1], _l[idx]
    return _l

def bubble_sort2(l, key=None):
    """バブルソート"""
    _l = l[:]
    sorted_pos = len(l) - 1

    if key is None:
        for n in range(sorted_pos):
            for idx in range(sorted_pos - n):
                if _l[idx] > _l[idx+1]:
                    _l[idx], _l[idx+1] = _l[idx+1], _l[idx]
    else:
        comparator = key
        for n in range(sorted_pos):
            for idx in range(sorted_pos - n):
                if comparator(_l[idx], _l[idx+1]):
                    _l[idx], _l[idx+1] = _l[idx+1], _l[idx]
    return _l

def insertion_sort(l):
    """挿入ソート"""
    for pos in range(1, len(l)):
        _insert(l, pos, l[pos])
    return l

def _insert(l, pos, val):
    i = pos - 1
    while i >= 0 and l[i] > val:
        l[i+1] = l[i]
        i = i - 1
        l[i+1] = val

def selection_sort(l):
    """選択ソート"""
    _l = l[:]
    for i in range(len(_l)-1):
        left = i
        for x in range(i+1, len(_l)):
            if _l[left] > _l[x]:
                left = x
            temp = _l[i]
            _l[i] = _l[left]
            _l[left] = temp
    return _l

def heap_sort(l):
    """ヒープソート"""
    _l = l[:]
    _build_heap(_l)
    for i in reversed(range(1, len(_l)-1)):
        temp = _l[0]
        _l[0] = _l[i]
        _l[i] = temp
        _heap(_l, 0, i)
    return _l

def _build_heap(l):
    for i in reversed(range((len(l)//2-1))):
        _heap(l, i, len(l))

def _heap(l, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and l[left] > l[i]:
        largest = left
    if right < n and l[right] > l[largest]:
        largest = right
    if largest != i:
        temp = l[i]
        l[i] = l[largest]
        l[largest] = temp
        _heap(l, largest, n)
