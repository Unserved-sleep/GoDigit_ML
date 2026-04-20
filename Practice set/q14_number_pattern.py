number_pattern: int = int(input())

def pattern(number):
    while number > 9:
        a = number % 10
        number //= 10
        b = number % 10
        number //= 10
        if a <= b:
            return False
    return True

print(pattern(number_pattern))

