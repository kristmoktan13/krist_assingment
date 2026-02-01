def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
my_list = [5, 9, 13, 27, 75]
result = sum_of_list(my_list)
print(f"The list: {my_list}")
print(f"The sum of the list is: {result}")