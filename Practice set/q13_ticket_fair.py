distance: int = int(input())
fare = distance * 2
age: int = int(input())
if age <= 12:
    fare -= fare * 0.5
if age > 62:
    fare -= fare * 0.3
print(fare)