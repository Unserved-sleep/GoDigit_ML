import re

password = input()

strength = lambda x: "STRONG" if re.match(r"^((?=.*[A-Z])(?=.*[0-9]).){8,}$",password) else "WEAK"
print(strength(password))