capacity: int = 1000
n: int = int(input())
count = 0
inflow = []
for _ in range(n):
    inflow.append(int(input()))

for i in inflow:
    capacity -= i
    count += 1
    if capacity <= 0:
        print(count)
        break
