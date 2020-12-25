"""
    [DESCRIPTION]: This is the fifth python sample.

    Link below [PEP-8 -- Style Guide for Python Code]:
    https://www.python.org/dev/peps/pep-0008/

    PEP(Python Enhancement Proposal): for proper styling of python code.

    This is a small sample of code where we run through set operations.

    [REMEMBER]: In Python we can work with (set) objects or (frozenset) obects,
                the difference between a (set) & (frozenset) is that a (frozenset)
                is immutable after the sets have been transformed.
"""
# Write a few initialized test sets.
set_a = [4, 7, 2, 1, 0, -5]
set_b = [6, 1, 8, 0]

set_a2 = [100, 200, 300, 400, 500]
set_b2 = [300, 400, 500]

set_a3 = ['a', 2, 'D', 100, -40, '#']
set_b3 = ['$', 30, 'A', 'X', 2, '.']

set_a4 = [2, 3, 4]
set_b4 = [4, 5, 6]

continue_set_operations = True
option = ''

while (continue_set_operations):
    try:
        print("a. Calculate the sets cardinality (LENGTH).")
        print("b. Check for value in the sets (A in B).")
        print("c. Check for a value NOT in the set (!A in B).")
        print("d. Check for no common elements (DISJOINT)")
        print("e. Check set 'A' & 'B' for a (SUBSET).")
        print("f. Check set 'A' & 'B' for a (SUPERSET).")
        print("g. Collect the (UNION) of set 'A' & 'B'.")
        print("h. Collect the (INTERSECTION) of set 'A' and 'B'.")
        print("i. Collect the (DIFFERENCE) of set 'A' & 'B'")
        print("j. Quit.\n")
        option = input("Enter in a letter: ")

        # Check to make sure that we are writing a alpha character.
        if (option.isalpha() == False):
            print("\n\t[ERROR]: Must be a letter !\n")

        # Convert the option to lowercase to make sure we have consistancy
        # when comparing the option that the user entered.
        lower_option = option.lower()
        if (lower_option == 'a'):
            frozen_1 = frozenset(set_a)
            cardinality = frozen_1.__len__()
            print("\n\tThe cardinality of the set is: {0}\n".format(cardinality))
        elif (lower_option == 'b'):
            frozen_2 = frozenset(set_a)
            value_to_check = 4
            result = value_to_check in frozen_2
            print("\n\tThe value {0} discovered in the set: {1}\n".format(value_to_check, result))
        elif (lower_option == 'c'):
            frozen_4 = frozenset(set_b)
            value_to_check = -1
            result = value_to_check not in frozen_4
            print("\n\tThe value {0} (NOT) discovered in the set: {1}\n".format(value_to_check, result))
        elif (lower_option == 'd'):
            frozen_6 = frozenset(set_a2)
            frozen_7 = frozenset(set_b2)
            disjoint = frozen_6.isdisjoint(frozen_7)
            print("\n\tSets are disjoint: {0}\n".format(disjoint))
        elif (lower_option == 'e'):
            frozen_8 = frozenset(set_a2)
            frozen_9 = frozenset(set_b2)
            subset = frozen_9.issubset(frozen_8)
            print("\n\tSet is a subset: {0}\n".format(subset))
        elif (lower_option == 'f'):
            frozen_10 = frozenset(set_a2)
            frozen_11 = frozenset(set_b2)
            superset = frozen_10.issuperset(frozen_11)
            print("\n\tSet is a superset: {0}\n".format(superset))
        elif (lower_option == 'g'):
            frozen_12 = frozenset(set_a3)
            frozen_13 = frozenset(set_b3)
            union = frozen_12.union(frozen_13)
            print("\n\tUnion of the set: {0}\n".format(union))
        elif (lower_option == 'h'):
            frozen_14 = frozenset(set_a3)
            frozen_15 = frozenset(set_b3)
            intersection = frozen_14.intersection(frozen_15)
            print("\n\tIntersection of the set: {0}\n".format(intersection))
        elif (lower_option == 'i'):
            frozen_16 = frozenset(set_a4)
            frozen_17 = frozenset(set_b4)
            difference = frozen_16.difference(frozen_17)
            print("\n\tDifference of the set: {0}\n".format(difference))
        elif (lower_option == 'j'):
            break
    except ValueError:
        print("Only lowercase letter (selections) from letters [a - i] please !")