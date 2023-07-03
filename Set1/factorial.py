def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 6
factorial_result = factorial(num)
print(f"Factorial of {num} is {factorial_result}.")