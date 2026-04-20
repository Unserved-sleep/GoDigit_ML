import re

text1 = "I have 2 apples and 5 oranges. 23 345 45.5 5.6   5,6"
print(re.findall(r'\d+', text1)) #digits
print(re.findall(r'\d{2}', text1))
print(re.findall(r'\D+', text1)) #non digits
print(re.findall(r'\D{3}', text1))
print(re.findall(r'\s+', text1)) #space
print(re.findall(r'\s{2}', text1))
print(re.findall(r'\S{2}', text1)) #non space
print(re.findall(r'\w{3}', text1)) #word-alphanumeric
print(re.findall(r'\W{2}', text1))
print(re.findall("[a-z]+", text1)) #alphabets
print(re.findall("[a-zA-z]+", text1))
print(re.match(r"^I ha", text1)) #start with
print(re.search(r"5,6$", text1)) #ends on
print(re.sub(r"\d+", "X", text1)) #replaceing
print(re.split(r"\s+", text1)) #split
email = "abc123@gmail.com"
print(re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email)) #gmail
print(re.findall(r"[\w.-]+@gmail\.\w+", email))
