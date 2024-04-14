def process_numbers():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    result = []

    for num in range(start, end + 1):
        if num % 2 == 0:
            result.append(num * 2)
        else:
            result.append(num ** 2)

    return result

processed_list = process_numbers()
print("Processed list:", processed_list)