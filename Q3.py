import random

A = [random.randint(0,100) for _ in range (20)]
B = list(range(20))

def extremept(arr):
    n = len(arr)
    extreme_points = []

    for i in range (1,n-1):
        if (arr[i-1] >arr[i] < arr[i+1]) or (arr[i-1] <arr[i] > arr[i+1]): #extreme point conditions
            extreme_points.append(arr[i])

    if extreme_points:
        print("Extreme points found: ",", ".join(str(x) for x in extreme_points))
    else:
        print("SORTED")

print(f"Array A:{A}")
extremept(A)
print("\n")
print(f"Array B:{B}")
extremept(B)