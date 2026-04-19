import re

quote = "I scream, you scream, we all scream for ice cream."

print(re.search("scream", quote))

print(re.findall("scream", quote))

print(re.split(",", quote))