import random
count = int(input("How many dice to roll? "))
total = 0
for _ in range(count):
    roll = random.randint(1, 6)
    total += roll
print(f"The sum of the {count} dice is: {total}")