from __future__ import print_function
import re

base8 = r"0[0-7]*"
base10 = r"\d\d*"
base16 = r"0[xX]\w+"
matched = re.search(base10, "12345")
try:
    print("matched ", matched.group(0))
except AttributeError:
    print("not matched")
