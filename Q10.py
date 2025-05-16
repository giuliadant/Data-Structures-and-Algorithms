import random

numbers = [random.randint(0,100) for _ in range (40)]

def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]  #base case
    else:
        max_of_rest = find_max_recursive(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

recursive_max = find_max_recursive(numbers)
built_in_max = max(numbers)

print(f"List: {numbers}")
print(f"Largest number in the list is: {recursive_max}")


if recursive_max == built_in_max:
    print("The result is correct.")
else:
    print(" Error: The result does not match the built-in max().")
