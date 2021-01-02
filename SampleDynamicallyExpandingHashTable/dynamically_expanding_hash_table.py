"""
    [DESCRIPTION]: This is sample #9 for python.

    NOTE: When launching this application launch through command-prompt rather than
          the nested command-line in a text editor such as vscode because the output
          of the console project wont update as well as runnning it through the command prompt.

    This is a custom hash table that dynamically expands but does not push to a
    separate linked list so it is NOT a open addressed table but rather a closed address table that
    deals with collisions through linear collision handling and instead of pushing to another linked list
    we will just linear probe to the next available entry.

    This is not a full implementation just something fun to build which would include a different
    approach to a hash table algorithm as well as a different interface such as nested classes and nested
    functions.

    This file makes use of the "Special Data Methods" which we overwrite and make use of.
    In this sample we also show a different way to handle input/output using the module "import sys."
"""
__title__ = "Sample Nine."
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

import sys

class DynamicallyExpandingHashTable:
    """
    Name        :   DynamicallyExpandingHashTable
    Purpose     :   This class will hold methods that will control the
                    dynnamically expanding hash table.
    """

    _expand_after = 3/4

    class Bucket:
        """
        Name        :   Bucket
        Purpose     :   This is the blueprint as to what the bucket will hold.
        """ 

        # Empty constructor.
        def __init__(self):
            pass

        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __str__(self):
            message = "\n\tKey: {0}\n\tValue: {1}".format(self.key, self.value)
            return message
        

    def __init__(self, initial_size):
        # The size we expand by is also just as important as the inital size.
        self.expanded_size = initial_size
        self.local_copy_of_size = initial_size
        self.default_size = initial_size
        self.number_of_filled_entries = 1
        self.table = [None] * self.default_size

    # Expands the hash table after the load factor has been met.
    def expand_table(self):
        # Double hash the entries now the table is x2 larger.
        self.default_size *= 2
        self.expanded_size = self.default_size

        # -- [ Nested Method ] ---------------------------------------
        def initialize_temp_table(self, temp_table):
            for buckets in range(0, self.expanded_size):
                temp_table.append(None)
            return temp_table

        # Call the nested function.
        # This is the temp list to write all of the current entries in.
        new_temp_table = []
        new_temp_table = initialize_temp_table(self, new_temp_table)

        # -- [ Another Nested Method ] -------------------------------
        def copy_entries_to_expanded_table(self, old_table, new_table):
            records = 0
            while (records < self.local_copy_of_size):
                new_table[records] = old_table[records]
                records += 1
            return new_table

        # Call the second nested function.
        new_temp_table = copy_entries_to_expanded_table(self, self.table, new_temp_table)
        return new_temp_table

    # This will calculate the new load factor every time there is a new entry made.
    def calculate_current_load_factor(self):
        curr_load_factor = self.number_of_filled_entries / self.default_size
        return curr_load_factor

    # Inserts a single bucket into the hash table.
    def bucket_insertion(self, key):
        # Calculate load factor.
        calculated_load_factor = self.calculate_current_load_factor()
        if (calculated_load_factor > self._expand_after):
            print("\n\t************************** TABLE EXPANSION **************************")
            self.table = self.expand_table()

        # Calculate the value at which this entry may sit.
        hash_value = hash(key) % self.default_size

        # Check the calculated position to see if it is filled.
        if (self.table[hash_value] is not None):
            # Linear probe.
            count_buckets = 0
            while (self.table[hash_value] is not None):
                # Do we have empty spots available?
                if (count_buckets == self.default_size):
                    return None
                hash_value += 1
                count_buckets += 1
            
            # We have found an empty position fill the node and insert.
            # We must use self when calling the nested class because it is
            # nested inside of the DynamicallyExpandingHashTable.
            new_node = self.Bucket(key, hash_value)
            self.table[hash_value] = new_node
            self.number_of_filled_entries += 1
            return self.table
        else:
            new_node = self.Bucket(key, hash_value)
            self.table[hash_value] = new_node
            self.number_of_filled_entries += 1
        return self.table

    # Deletes a single bucket.
    def delete_bucket(self, key):
        bucket_position = hash(key) % self.default_size
        del self.table[bucket_position]
        self.number_of_filled_entries -= 1
        self.default_size -= 1
        return None

    # This is just to display the size which is 1 less than recorded.
    def __len__(self):
        return self.number_of_filled_entries - 1

    # Displays all key value pairs in the __str__ class readable representation
    # written in class Bucket().
    def show_key_value_pairs(self):
        print("\n  -- Entries --")
        entries = 0
        while (entries < self.default_size):
            if (self.table[entries] is not None):
                print(self.table[entries])
            entries += 1

if __name__ == "__main__":
    # When initializing the hash table the size matters !
    # It is good to start with a prime number larger than 10 for example.
    # It would be a good idea to research what potential sizes would be best for a closed
    # or open addressed table.
    _initial_size_of_hash_table = 13
    hash_methods = DynamicallyExpandingHashTable(_initial_size_of_hash_table)

    write_to_table = True
    while (write_to_table):
        try:
            # Showing a different way of printing to the screen.
            sys.stdout.write("\n  -- Menu --\n")
            sys.stdout.write("\t1. Insert new bucket.\n")
            sys.stdout.write("\t2. Delete a bucket.\n")
            sys.stdout.write("\t3. Show key value pairs.\n")
            sys.stdout.write("\t4. Display current size.\n")
            sys.stdout.write("\t5. Quit.\n\n")
            selection = int(input("\tEnter in a selection: "))
            # If we have a selection __eq__ to five then quit.
            if (selection == 5):
                break
            
            # Compare the selections.
            if (selection == 1):
                name_to_hash = input("\nEnter in a name to hash: ")
                # Calculate the hash value.
                hash_methods.bucket_insertion(name_to_hash)
            elif (selection == 2):
                who_to_delete = input("\nEnter in a name to delete: ")
                hash_methods.delete_bucket(who_to_delete)
            elif (selection == 3):
                hash_methods.show_key_value_pairs()
            elif (selection == 4):
                # We overwrote the __len__() class method so when we call is as a function it will
                # run what was written in the new definition of the __len__() method.
                print("\n\t\tThe current size of the hash table is: [{0}]".format(hash_methods.__len__()))
            else:
                print("\n\tOut of range of selections to choose from !")
        except ValueError:
            # This is the standard error stream and if we have a character we
            # must flush this out of the stdin buffer otherwise we will get an infinite loop
            # in some languages.
            sys.stderr.write("\n\tNo characters allowed, Only numbers.\n")
            sys.stdin.flush()
    