import random

array = [random.randint(0,100) for _ in range (50)]

def find_duplicates(arr):
    counts = {}
    duplicates = set()

    for num in arr:
        if num in counts:
            duplicates.add(num)
        else:
            counts[num] = 1

    return list(duplicates)

repeats = find_duplicates(array)

if all(array.count(x) > 1 for x in repeats):
    print(" Function passed for this array")
else:
    print("Function failed for this array")

print(f"Array: {array}")
print("Repeated integers:", repeats)
