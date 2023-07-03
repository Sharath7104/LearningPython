# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"

def calculate_sum_and_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

input_numbers = [10, 20, 30, 40]
sum_result, average_result = calculate_sum_and_average(input_numbers)
print(f"Sum: {sum_result}, Average: {average_result}")