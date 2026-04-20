drains_per_minute: int = int(input())
charge: int = 100
count = 0
while charge > 0:
    charge -= drains_per_minute
    count += 1

print(count)
