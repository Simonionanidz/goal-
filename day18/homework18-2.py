def filter_four_multiples(numbers):
    filtered_list = [num for num in numbers if num % 4 == 0]
    return filtered_list


numbers = list(range(1, 21))
filtered_numbers = filter_four_multiples(numbers)
print("Filtered list:", filtered_numbers)