from sqlalchemy import false

subjects = list(map(int, input().split()))

def status(subject):
    for i in subject:
        if i < 35:
            return False
    return True

if not status(subjects):
    print("Fail")
else:
    if sum(subjects) / len(subjects) >= 75:
        print("Distinction")
    else:
        print("Pass")