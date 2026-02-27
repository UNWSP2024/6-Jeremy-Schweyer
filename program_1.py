import random
dice = 1, 2, 3, 4, 5, 6
Total = 0


def randDice():
    random1 = random.choice(dice)
    random2 = random.choice(dice)
    return random1 + random2


for i in range(100):
    Total += randDice()

average = Total / 100
print("The average is: ", average)
