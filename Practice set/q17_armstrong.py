from copy import deepcopy

number: int = int(input("Enter a number: "))
total = 0
num = deepcopy(number)
while number > 0:
    total += (number % 10) ** 3
    number //= 10

if total == num:
    print("Armstrong number")