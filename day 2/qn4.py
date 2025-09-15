'''Problem 4
Write a Python program that:

Reads a list of names from the user (separated by spaces).
Sorts the names alphabetically and stores them in a list.
Converts the list into a tuple.
Saves the sorted list and tuple into a file named names_data.txt.
Reads and prints the saved data from the file.
'''


def process_names(input_line):
    # Split input, sort the names, and return as list and tuple
    name_list = sorted(input_line.split())
    name_tuple = tuple(name_list)
    return name_list, name_tuple

# Step 1: Read user input
names_input = input("Enter a list of names (space-separated): ")

# Step 2: Process input
sorted_list, sorted_tuple = process_names(names_input)

# Step 3: Display sorted names
print("Sorted List of Names:", sorted_list)
print("Sorted Tuple of Names:", sorted_tuple)

# Step 4: Save to file
filename = 'names_data.txt'
with open(filename, 'w') as file:
    file.write("Sorted List: " + ', '.join(sorted_list) + '\n')
    file.write("Sorted Tuple: " + ', '.join(sorted_tuple) + '\n')

# Step 5: Read and print the file content
print("\nData read from file:")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())
