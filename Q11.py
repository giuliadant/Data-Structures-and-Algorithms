import math

def maclaurin(x, n, func): #x is angle in radians, n is number of terms,function set default to sin inside maclaurin
    result = 0.0
    term = x if func =='sin' else 1.0  # first term
    result= result + term
    sign = -1 #alternate sign

    for i in range(1, n): #remaining terms
        power = 2 * i + 1 if func == 'sin' else 2 * i #calculates exponent
        term *= x * x / ((power - 1) * power)  # incremental factorial calculation
        result = result + sign * term
        sign *= -1  # flips sign for next term

    return result

x = math.pi / 2
func = 'sin'
approx = maclaurin(x, 10, func)
actual = math.sin(x) if func == 'sin' else math.cos(x)

print(f"Approximation: {approx}")
print(f"Actual value: {actual}")
print(f"Error: {abs(approx - actual)}")