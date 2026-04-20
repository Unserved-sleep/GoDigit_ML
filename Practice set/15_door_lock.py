def door_lock(pin,attempts):
    if pin == attempts:
        return True
    return False

correct_pin: int = int(input())
attempt1: int = int(input())
attempt2: int = int(input())
attempt3: int = int(input())
if door_lock(correct_pin,attempt1):
    print("Access granted")
elif door_lock(correct_pin,attempt2):
    print("Access granted")
elif door_lock(correct_pin,attempt3):
    print("Access granted")
else:
    print("Locked")
