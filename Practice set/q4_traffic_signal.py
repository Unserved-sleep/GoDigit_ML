cycle: int = int(input())

while cycle > 0:
    cycle -= 30
    if cycle <= 0:
        print("Red")
        break
    cycle -= 15
    if cycle <= 0:
        print("Yellow")
        break
    cycle -= 45
    if cycle <= 0:
        print("Green")
        break