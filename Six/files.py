"""
    [DESCRIPTION]: This is sample file #6 for python.

    Just a simple sample of the use of read only permission python files.
    Using the 2 different methods to perform read only operations.
"""
__title__ = "Sample Six"
__author__ = "Braiden Gole"
__version__ = "1.0.0"

print()
# Open a file using the with statement so we do
# not have to worry about closing the file. (SAFEST BET)
with open("input.txt", "r") as input_file:
    data = input_file.readlines()
    print(data)

# We can prove to ourselves that the file is close by running a test.
# The test being that the .close function returns a boolean either True or False
# and we can check to see if it is True and if so then the file has been closed.
print("\nIs the input.txt closed: {0}\n".format(input_file.closed))

# Second Method of opening a file.
our_file = open("input.txt", "r")
file_content = our_file.readline()
print(file_content)
print("\nIs input.txt closed now: {0}".format(our_file.closed))
our_file.close()

# This will now output True because the file has closed.
print("\nFinal check on input.txt closed: {0}\n".format(our_file.closed))
