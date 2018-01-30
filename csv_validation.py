# coding: utf-8

"""
csvのバリデーション
"""

from __future__ import print_function
import re

def genarate_lines(filename):
    """ファイルを行単位でyieldするジェネレータ"""
    with open(filename) as all_lines:
        for line in all_lines:
            yield line

def validate_csv(filename, comment=False):
    """
    csvがフォーマットに準拠しているか判定する
    オプション引数comment=Trueとすると先頭が#で始まる行の処理をスキップする
    """
    START, VALUE, FIRSTQ, SECONDQ, RETURN, ERROR = range(6)
    states = ["START", "VALUE", "FIRSTQ", "SECONDQ", "RETURN", "ERROR"]
    states_table = dict(zip(list(range(6)), states))
    init_state = START
    transitions = {
            START: {r",": START, r"\"": FIRSTQ, r"\n": RETURN, r"[^,\"]": VALUE},
            VALUE: {r"[^,]": VALUE, r"\n": RETURN, r",": START},
            FIRSTQ: {r"[^\"]": FIRSTQ, r"\"": SECONDQ},
            SECONDQ: {r"[^,\"\n]": ERROR, r",": START, r"\n": RETURN, r"\"": FIRSTQ}
            # RETURN: {r"\n": START}
            }
    state = init_state
    for line in genarate_lines(filename):
        if comment and line.startswith("#"):
            continue
        for char in line:
            print(states_table[state], char)
            transition_regexp = transitions[state]
            for regexp, s in transition_regexp.items():
                matched = re.match(regexp, char)
                if matched is not None:
                    state = s
                if state == ERROR:
                    return False
        else:
            state = init_state
    return True

def validate_csv2(filename, comment=True):
    """
    正規表現を使用しないバージョン
    """
    START, VALUE, FIRSTQ, SECONDQ, RETURN, ERROR = range(6)
    states = ["START", "VALUE", "FIRSTQ", "SECONDQ", "RETURN", "ERROR"]
    states_table = dict(zip(list(range(6)), states))
    init_state = START
    transitions = {
            START: {",": START, "\"": FIRSTQ, "\n": RETURN, (",", "\\"): VALUE},
            VALUE: {(","): VALUE, "\n": RETURN, ",": START},
            FIRSTQ: {("\""): FIRSTQ, "\"": SECONDQ},
            SECONDQ: {(",", "\"", "\n"): ERROR, ",": START, "\n": RETURN, "\"": FIRSTQ}
            }
    state = init_state
    for line in genarate_lines(filename):
        if comment and line.startswith("#"):
            continue
        for char in line:
            print(states_table[state], char)
            transition = transitions[state]
            for rule, s in transition.items():
                if isinstance(rule, tuple):
                    for r in rule:
                        if char == r:
                            state = s
                elif char == rule:
                    state = s

                if state == ERROR:
                    return False
        else:
            state = init_state
    return True


if __name__ == "__main__":
    if validate_csv("sample.csv", comment=True):
    # if validate_csv2("sample.csv", comment=True):
        print("accept")
    else:
        print("error")
