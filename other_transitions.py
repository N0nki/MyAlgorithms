START, VALUE1, VALUE2, FIRSTQ, SECONDQ, RETURN, ERROR = range(7)
states = ["START", "VALUE1", "VALUE2", "FIRSTQ", "SECONDQ", "RETURN", "ERROR"]
states_table = dict(zip(list(range(7)), states))
transitions = {
        START: {r",": START, r"\"": FIRSTQ, r"\n": RETURN, r"[^,\"]": VALUE1},
        VALUE1: {r"[^,]": VALUE1, r"\n": RETURN, r",": START},
        VALUE2: {r"[^\"]": VALUE2, r"\"": SECONDQ},
        FIRSTQ: {r"[^\"]": VALUE2, r"\"": SECONDQ},
        SECONDQ: {r"[^,\"\n]": ERROR, r",": START, r"\n": RETURN, r"\"": FIRSTQ},
        RETURN: {r".": START}
        }

