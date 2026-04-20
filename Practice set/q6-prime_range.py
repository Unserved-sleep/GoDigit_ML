A, B = map(int, input().split())
count =0

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(A, B+1):
    if is_prime(i):
        count += 1

print(count)