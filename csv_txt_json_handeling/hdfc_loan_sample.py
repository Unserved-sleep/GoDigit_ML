import json
import csv

with open("C:\\Users\\Admin\\Downloads\\hdfc_ls.json", 'r', encoding='utf-8') as f:
    loan = json.load(f)

print(type(loan))
print(loan)

for line in loan:
    print(line)

print(type(loan[0]))

with open("C:\\Users\\Admin\\Downloads\\hdfc_ls.csv", 'w', newline='', encoding='utf-8') as f_csv:
    fc = csv.DictWriter(f_csv, fieldnames=loan[0].keys())

    fc.writeheader()
    fc.writerows(loan)