def sum_greater_than_10(numbers):
    total_sum = 0
    for num in numbers:
        if num > 10:
            total_sum += num
    return total_sum


input_numbers = [5, 12, 8, 15, 3, 10, 20]
result = sum_greater_than_10(input_numbers)
print("Sum of numbers greater than 10:", result)