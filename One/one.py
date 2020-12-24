"""
    [ DESCRIPTION ]: This is the first sample file
                     of python and I would like to mention
                     that when writing Python 3 code I will
                     do my best to stay on tract with proper
                     style from the PEP Styling index.
    
    Link below [PEP-8 -- Style Guide for Python Code]:
        https://www.python.org/dev/peps/pep-0008/

    Always follow the PEP(Python Enhancement Proposal)
    for proper styling of python code.
"""
__title__ = "Sample One."
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

# Declaring python dictionary.
hex_bin_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

# Get the lowest and highest values both value and key.
lowestHexValue = min(zip(hex_bin_map.values(), hex_bin_map.keys()))
highestHexValue = max(zip(hex_bin_map.values(), hex_bin_map.keys()))
print(lowestHexValue)
print(highestHexValue)

# Output the entire map using a one-line for loop.
entire_map = [value for value in hex_bin_map]
print(entire_map)

# Create a list of cubed values.
print("\n-- List of cubed values ! --")
list_of_cubed_values = list(map(lambda num: num ** 3, range(2, 40)))
print("\n", list_of_cubed_values)

# Design a crazy list using list comprehension... All possibilities !
crazy_list = [(x, y) for x in ['B', 'A', 'C', 'Z'] for y in ['Q', 'B', 'G'] if x != y]
print(crazy_list)

# Print a set of even numbers starting from 0 to 20. Print these numbers
# on a different line.
print("\nEven Numbers:")
for nums in range(0, 20, 2):
    print(nums);

# Print a set of odd numbers starting from 0 to 20. Print these numbers
# on the same line.
print("\nOdd Numbers:")
for oddNums in range(0, 20, 3):
    print(oddNums, end="")