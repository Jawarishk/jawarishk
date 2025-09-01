import random

num_dice = int(input("How many dice to roll? "))
total = 0

for i in range(num_dice):
    roll = random.randint(1, 6)
    total += roll

print(total)