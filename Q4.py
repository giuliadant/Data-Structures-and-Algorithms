import random

numbers = [random.randint(1,1024) for _ in range (80)]
prime = [1,3,5,7,11,13]

def find_2_pairs(numbers):
    product_dict = {} #empty dictionary dynamically filled in later using products of pairs as keys
    seen_2_pairs = set() #set to store 2-pairs we've already found and added to result to avoid duplicates
    result = [] #stores 2-pairs of integers

    n = len(numbers)
    for i in range(n): #iterates from 0 till n-1 (end of array)
        for j in range(i + 1, n): #iterates from i+1 till n-1 (last element)
            a, b = sorted((numbers[i], numbers[j]))
            product = a * b
            if product not in product_dict:
                product_dict[product] = [] #adds product as a new key to product_dict
            product_dict[product].append((a, b))

    for product, pairs in product_dict.items(): #iterates through each key-value pair in product_dict
        if len(pairs) >= 2:
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    pair1 = tuple(pairs[i])
                    pair2 = tuple(pairs[j])
                    a, b = pair1
                    c, d = pair2

                    if len({a,b,c,d}) == 4:
                        #ensure all four numbers are distinct
                        sorted_2_pair = tuple(sorted((pair1, pair2)))
                        if sorted_2_pair not in seen_2_pairs:
                            result.append((list(pair1), list(pair2))) #store as lists for output
                            seen_2_pairs.add(sorted_2_pair)

    return result

def test_find_2_pairs(arr, name="Array"):
    pairs = find_2_pairs(arr)
    print(f"\nTesting {name}:")
    if pairs:
        print(f" Found {len(pairs)} pair(s):")
        for pair in pairs:
            print(f"  {pair}")
    else:
        print(" No found pairs.")

test_find_2_pairs(numbers, "numbers")
test_find_2_pairs(prime, "prime")
#new array added would be tested here
