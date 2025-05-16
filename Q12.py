import random
from sympy import fibonacci

n = random.randint(0, 100)
print(f"Number of terms: {n}")

def fibonacci_sum(n):
    if n <= 0:
        print("Fibonacci sequence: []")
        return 0
    elif n == 1:
        print("Fibonacci sequence: [1]")
        return 1

    a, b = 1, 1
    sequence = [a, b]
    total = a + b

    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(b)
        total += b

    print(f"Fibonacci sequence: {sequence}")
    return total

# Store result once
result = fibonacci_sum(n)

expected = fibonacci(n + 2) - 1
print(f"Expected (SymPy): {expected}")
print(f"Fibonacci sum of first {n} terms: {result} {'(Matches Expected)' if result == expected else 'Mismatch'}")




