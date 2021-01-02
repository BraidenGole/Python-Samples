"""
    [DESCRIPTION]: This is sample python #10.

    I have initialized a list with nested tuples that extract or slice
    different sections of data based on the context desired such as
    alphabetical order where this would only have to do with names and
    not numbers.
"""
__title__ = "Sample Ten"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

import itertools
from collections import defaultdict

class DataSlicer:
    """
    Name        :   DataSlicer
    Purpose     :   This class will hold methods that take specific
                    slices of data from the initialized tuple.
    """

    def __init__(self, data_chunk):
        self.data_chunk = data_chunk

    # Yields a set of sorted users names.
    def generate_alphabetical_name_chunk(self):
        t = itertools
        self.data_chunk.sort(key=lambda chunk_name: chunk_name["Name"])
        for names, blank in t.groupby(self.data_chunk, key=lambda chunk_name: chunk_name["Name"]):
            yield names
        yield None

    # Yields a set of users based on a specified country.
    def generate_specific_country_chunk(self, filter_country):
        # defaultdict lets use give the ket a default value.
        data_pool = defaultdict(list)
        for countries in self.data_chunk:
            data_pool[countries["Country"]].append(countries)
        
        # Filter the country you would like.
        for items in data_pool[filter_country]:
            yield items
        return None

    # Output a specific chunk of data.
    @staticmethod
    def output_specific_chunk(specific, data_title):
        print("\n -- List of [{0}] --".format(data_title))
        for item in specific:
            print(item)
        print("\n-- End list of [{0}] --".format(data_title))
        return None

    # Output a single entry at a time by pressing enter for the next entry.
    def one_chunk_at_a_time(self):
        print("\n  -- Start listing single chunk --")
        for data in range(len(self.data_chunk)):
            print("\n\t\t", self.data_chunk[data])
            blank_input = input("\n\tPress | ENTER | or QUIT: ")
            termination = blank_input.upper()
            if (termination == "QUIT"):
                return None
        print("\nWe have reached the end of the list !\n")

    # Simply outputs all data in chunk.
    def output_entire_chunk(self):
        for data in range(len(self.data_chunk)):
            print(self.data_chunk[data])
        return None


if __name__ == "__main__":
    # Initialized chunk of data to slice from.
    chunk = [
        {"ID": 1, "Name": "John", "Email": "john32@gmail.com", "Country": "Canada",},
        {"ID": 2, "Name": "Sean", "Email": "sean_emerie", "Country": "Vancover",},
        {"ID": 3, "Name": "Shannon", "Email": "shannon_101@hotmail.com", "Country": "Germany",},
        {"ID": 4, "Name": "Kayla", "Email": "Kay_kay12@gmail.com", "Country": "Canada",},
        {"ID": 5, "Name": "Steven", "Email": "steve@yahoo.com", "Country": "Germany",},
        {"ID": 6, "Name": "Dan", "Email": "DanTheMan@yahoo.com", "Country": "Vancover",},
        {"ID": 7, "Name": "Bob", "Email": "bobbyBoy123@hotmail.com", "Country": "Canada",},
        {"ID": 8, "Name": "Andrew", "Email": "andy34@gmail.com", "Country": "Germany",},
        {"ID": 9, "Name": "Kim", "Email": "workoutGirl546@gmail.com", "Country": "Vancover",},
        {"ID": 10, "Name": "David", "Email": "sifu_kung_fu90@gmail.com", "Country": "Canada",},
        {"ID": 11, "Name": "Brant", "Email": "businessMan@yahoo.com", "Country": "Vancover",},
        {"ID": 12, "Name": "Justin", "Email": "longBoarder@gmail.com", "Country": "Germany",},
        {"ID": 13, "Name": "Lori", "Email": "lor_f123@hotmai.com", "Country": "Vancover",},
        {"ID": 14, "Name": "Jason", "Email": "bankManagerCibc@yeahoo.com", "Country": "Canada",},
        {"ID": 15, "Name": "Anna", "Email": "anna_v_178@gmail.com", "Country": "Vancover",},
        {"ID": 16, "Name": "Veronica", "Email": "Skater101Girl@gmail.com", "Country": "Vancover",},
        {"ID": 17, "Name": "Eddie", "Email": "eddie@hotmail.com", "Country": "Germany",},
        {"ID": 18, "Name": "Cody", "Email": "codester_f@gmail.com", "Country": "Vancover",},
        {"ID": 19, "Name": "Robbie", "Email": "hockey_guy55@yahoo.com", "Country": "Vancover",},
        {"ID": 20, "Name": "Random_user", "Email": "random_user@gmail.com", "Country": "Canada",},
    ]

    # Initialize the object.
    initialized_chunk = DataSlicer(chunk)
    
    # Generate a list of names from the data set.
    set_of_names = initialized_chunk.generate_alphabetical_name_chunk()

    # Generate a list of users based on the filtered country.
    _country_to_filter = "Canada"
    specified_countries = initialized_chunk.generate_specific_country_chunk(_country_to_filter)

    # Output functions to output a specific chunk of data.
    #initialized_chunk.output_specific_chunk(set_of_names, "Names")
    #initialized_chunk.output_specific_chunk(specified_countries, "Specified Countries")

    # Ouput functions to display the entire set of data in two ways
    # either one at a time or all at once.
    #initialized_chunk.one_chunk_at_a_time()
    #initialized_chunk.output_entire_chunk()