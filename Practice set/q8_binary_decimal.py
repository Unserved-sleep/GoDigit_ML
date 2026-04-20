binary_num: int = int(input())
number = 0
power = 0
while binary_num > 0:
    number += (binary_num %10)*2**power
    power += 1
    binary_num //= 10

print(number)