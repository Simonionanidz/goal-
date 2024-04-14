def remove_duplicates(numbers):
    return list(set(numbers))


numbers = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9]
filtered_numbers = remove_duplicates(numbers)
print("Filtered numbers:", filtered_numbers)