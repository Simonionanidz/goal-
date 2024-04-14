def lengths_of_strings(string_list):
    lengths_list = []
    for string in string_list:
        lengths_list.append(len(string))
    return lengths_list


input_strings = ["apple", "banana", "orange", "kiwi", "strawberry"]
string_lengths = lengths_of_strings(input_strings)
print("Lengths of strings:", string_lengths)