seat: int = 40
n: int = int(input())
request = []
for _ in range(n):
    request.append(int(input()))

for i in request:
    seat -= i
    if seat <= 0:
        print("WAITLISTED")
    else:
        print("CONFIRMED")