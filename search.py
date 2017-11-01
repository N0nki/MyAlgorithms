# coding: utf-8

"""
サーチアルゴリズム
* リニアサーチ
* バイナリサーチ
"""

from __future__ import division
import sys

def liner_search(collection, elm):
    """リニアサーチ"""
    for e in collection:
        if e == elm:
            return True
    return False

def binary_search(collection, elm):
    """バイナリサーチ"""
    try:
        _abort_sorted(collection)
    except ValueError:
        sys.exit("collection must be sorted")

    left = 0
    right = len(collection) - 1

    while left <= right:
        mid = (left + right) // 2
        if elm < collection[mid]:
            right = mid - 1
        elif elm > collection[mid]:
            left = mid + 1
        else:
            return True
    return False

def index_liner(collection, elm):
    """リニアサーチで要素のインデックスを返す"""
    for idx,e in enumerate(collection):
        if e == elm:
            return idx
    raise ValueError("{} is not in collection".format(elm))

def index_binary(collection, elm):
    """バイナリサーチで要素のインデックスを返す"""
    try:
        _abort_sorted(collection)
    except ValueError:
        sys.exit("collection must be sorted")

    left = 0
    right = len(collection) - 1

    while left <= right:
        mid = (left + right) // 2
        if elm < collection[mid]:
            right = mid - 1
        elif elm > collection[mid]:
            left = mid + 1
        else:
            return mid
    raise ValueError("{} is not in collection".format(elm))

def _abort_sorted(collection):
    """collectionがソート済みかチェック"""

    if collection != sorted(collection):
        raise ValueError("collection nust be sorted")
    return True
