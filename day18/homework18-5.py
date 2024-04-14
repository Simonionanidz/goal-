def average_of_list(numbers):
    if len(numbers) == 0:
        return 0  
    else:
        return sum(numbers) / len(numbers)  


numbers = [2, 4, 6, 8, 10]
average = average_of_list(numbers)
print("Average:", average)