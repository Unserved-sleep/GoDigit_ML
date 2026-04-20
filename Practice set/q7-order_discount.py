amount: int = int(input())

if amount >= 5000:
    amount -= amount * 0.2
elif amount >= 3000:
    amount -= amount * 0.1
elif amount >= 1000:
    amount -= amount * 0.05

print(amount)