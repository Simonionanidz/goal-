def square_numbers(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num ** 2)
    return squared_list


input_numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(input_numbers)
print("Squared numbers:", squared_numbers)