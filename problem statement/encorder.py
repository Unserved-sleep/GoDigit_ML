import re
from collections import defaultdict

from sympy.testing.pytest import raises

sentence: str = str(input(""))
try:
    if re.search(r"A-Za-z", sentence):
    string_dict: dict[str, str] = dict(map(lambda char: (char, chr(ord(char)+2)) , sentence))
    else: raise Exception("Invalid Input")
except Exception as e:
    print(e)