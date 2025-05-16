def evaluate_rpn(expression):
    stack = []
    print(f"Initial stack:{stack}")

    for element in expression.split(): #splits each element in the expression
        if element in "+-x/": #if element is an operator
            b = int(stack.pop()) #pop the top two elements in correct order
            a = int(stack.pop())

            if element == "+":
                stack.append(a + b)
            elif element == "-":
                stack.append(a - b)
            elif element == "x":
                stack.append(a * b)
            elif element == "/":
                if b == 0: #handle division carefully to avoid division by zero
                    raise ValueError("Division by zero")
                stack.append(a / b)

        else: #if element is a number
            stack.append(float(element))
            print(f"Stack:{stack}")

    if len(stack) != 1: #final result should be the only item left on the stack
        raise ValueError("Invalid RPN expression")
    return stack[0]

expression = "10 5 - 1 + 4 x 3 /"
try:
    result = evaluate_rpn(expression)
    print(f"Stack: {result}")
except ValueError as e:
    print(f"Error: {e}")