import re

sentence: str = str(input(""))
string_dict: dict[str, str] = {}
try:
    if re.match(r"[A-Za-z]*", sentence):
        string_dict = dict(map(lambda char: (char, chr(ord(char)+2)) , sentence))
    else: raise Exception("Invalid Input")
except Exception as e:
    print(e)
print(string_dict)