import re

word: str = input("Enter a word: ")
print(len(re.findall(r'[aeiouAEIOU]', word)))
