from copy import deepcopy

number: int = int(input("Enter a number: "))
num = deepcopy(number)
reverse = 0
while number > 0:
    reverse *= 10
    reverse += (number % 10)
    number //= 10

print(reverse == num)