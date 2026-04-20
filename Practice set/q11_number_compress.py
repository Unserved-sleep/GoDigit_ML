number: int = int(input())
count = 0
while number > 1:
    if number % 2 == 0:
        count += 1
        number //= 2
    else:
        break
print(count)