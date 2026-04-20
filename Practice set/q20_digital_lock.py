number: int = int(input())

def calc_sum(x):
    s_um = 0
    while x > 0:
        s_um += (x % 10)
        x //= 10
    return s_um

number_sum = calc_sum(number)
while number > 9:
    number -= number_sum
    print(number)

print(number)
