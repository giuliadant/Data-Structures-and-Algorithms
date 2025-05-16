def sqrt_newton_raphson(n, tolerance=1e-6, max_iterations=1000):
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    x = n / 2 if n >= 2 else 1  # Initial guess

    for _ in range(max_iterations):
        next_x = 0.5 * (x + n / x)
        if abs(next_x - x) < tolerance:
            return next_x
        x = next_x
    return x  #return final approximation if not yet converged


try:
    n = float(input("Enter a number: "))
    result = sqrt_newton_raphson(n)
    print(f"Approximate square root is: {result}")
except ValueError as e:
    print("Error:", e)

