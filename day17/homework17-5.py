def filter_strings_starting_with_a(string_list):
    filtered_list = []
    for string in string_list:
        if string.startswith('a') or string.startswith('A'):  # Check if string starts with 'a' or 'A'
            filtered_list.append(string)
    return filtered_list

# Example usage:
input_strings = ["apple", "banana", "orange", "kiwi", "apricot", "grape"]
filtered_strings = filter_strings_starting_with_a(input_strings)
print("Strings starting with 'a':", filtered_strings)
