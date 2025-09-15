'''Problem 5
Write a Python program that:

Accepts a sequence of numbers from the user.
Stores the numbers in a list and finds the maximum and minimum values.
Stores the results (list, max, min) in a file named minmax_data.txt.
Reads and prints the saved data from the file.'''

def process_numbers(input_line):
    number_list = [int(num) for num in input_line.split()]
    max_val = max(number_list) if number_list else None
    min_val = min(number_list) if number_list else None
    
    return number_list, max_val, min_val

user_input = input("Enter a sequence of numbers (space-separated): ")
numbers, max_num, min_num = process_numbers(user_input)

print("Number List:", numbers)
print("Maximum:", max_num)
print("Minimum:", min_num)

filename = 'minmax_data.txt'
with open(filename, 'w') as file:
    file.write(f"Number List: {numbers}\n")
    file.write(f"Maximum: {max_num}\n")
    file.write(f"Minimum: {min_num}\n")

print("\nData read from file:")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())