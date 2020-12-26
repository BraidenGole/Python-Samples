"""
    [DESCRIPTIION]: This is sample file #7 for python.

    This is a sample on command-line arguments with python.

    [HOW TO PASS COMMAND-LINE ARGUMENTS]: Windows python <file_name.py> arg1 arg2 arg3

    If you want to pass in a string that has multiple spaces as ONE argument then we must
    encase the parameter with quotation marks otherwise they will be counted as two.

    [EXAMPLES]:
        python command_line.py "Braiden Gole" "Brant Gole" "Kim Gole" "Dave Gole"
        python command_line.py braiden gole brant gole kim gole dave gole
"""
__title__ = "Sample Seven"
__author__ = "Braiden Gole"
__version__ = "1.0.0"

import sys

name_of_program = sys.argv[0]
first_command_line_argument = sys.argv[1]
print("\n\tName of program: " + '[' + name_of_program + ']')
print("\tOur first command line argument: " + '[' + first_command_line_argument + "]\n")

# argv is a (list) which means this list has all the list methods attached such as .pop()

# We can even gather many arguments with a for loop.
print("\n-- Looping through command-line arguments --\t")
for args in range(len(sys.argv)):
    print('\t' + sys.argv[args])
