import re

text1 = "I have 2 apples and 5 oranges. 23 345 45.5 5.6  5,6"
print(re.findall(r'\d+', text1))
print(re.findall(r'\d{2}', text1))
print(re.findall(r'\D+', text1))
print(re.findall(r'\D{3}', text1))
print(re.findall(r'\s+', text1))
