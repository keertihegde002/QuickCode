def generate_substrings(string, index):
    if index == len(string):
        return []

    substrings = []
    for i in range(index, len(string)):
        substring = string[index:i+1]
        substrings.append(substring)
        substrings.extend(generate_substrings(string, i+1))

    return substrings

# Example usage
input_string = "abc"
all_substrings = generate_substrings(input_string, 0)
print(all_substrings)
