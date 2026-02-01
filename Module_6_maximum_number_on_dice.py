import random
def roll_dice(sides):
    return random.randint(1, sides)
max_number = int(input("Enter the number of sides on the dice: "))
result = 0
while result != max_number:
    result = roll_dice(max_number)
    print(f"Rolled: {result}")
