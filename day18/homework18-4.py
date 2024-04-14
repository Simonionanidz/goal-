def process_last_name(last_name):
    
    processed_list = [char.upper() for char in last_name]

    
    filtered_list = []
    for char in processed_list:
        if char not in ['A', 'E', 'I', 'O', 'U']:
            filtered_list.append(char)

    return filtered_list


last_name = input("Enter your last name: ")
processed_last_name = process_last_name(last_name)
print("Processed last name:", processed_last_name)