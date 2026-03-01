# 1. Iterative factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 2. Recursive factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

# 3. Multiple return values
def sum_and_difference(a, b):
    return a+b, a-b

# 4. Default parameter
def greet(name="Guest"):
    return f"Hello, {name}!"

# 5. *args example
def total_sum(*numbers):
    return sum(numbers)