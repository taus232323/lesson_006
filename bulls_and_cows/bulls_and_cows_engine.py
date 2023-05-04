import random

import random

conceived = None
bulls = {}
cows = {}

def conceive_number():
    global conceived
    while True:
        num = random.sample(range(0, 10), 4)
        if num[0] != 0:
            break
    conceived = str(num[0] * 1000 + num[1] * 100 + num[2] * 10 + num[3])
    # print(conceived)

def check_number(figure):
    global conceived, bulls, cows
    bulls = {figure: 0}
    cows = {figure: 0}
    for i in range(4):
        if figure[i] == conceived[i]:
            bulls[figure] += 1
        else:
            cows[figure] += 1
    print("быки - ", sum(bulls.values()), "коровы - ", sum(cows.values()))


def is_gameover():
    global bulls
    if sum(bulls.values()) == 4:
        return True
    else:
        return False





