def fibonacci(n):
    sequence = [0, 1]
    if n <= 2:
        return sequence[:n]
    for _ in range(n - 2):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

num = 5
fibonacci_sequence = fibonacci(num)
print(fibonacci_sequence)