import random

rolls = []
max_roll = 5
win = False
while max_roll:
    rolls.append(random.randrange(1,7))
    max_roll -= 1
    if rolls[-1] == 6:
        win = True
        break
if win:
    print('You won! Rolls: ', rolls)
else:
    print('Game Over')