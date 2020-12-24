"""
    [ DESCRIPTION ]: This is sample file #3 for python.

    Reference PEP-8 Styling Index: https://www.python.org/dev/peps/pep-0008/
"""
__title__ = "Sample Three."
__author__ = "Braiden Gole"
__version__ = "1.0.0"

# Constant global variables.
_standardHealth = 100
_standardShield = 0
_alive = True
_maxShield = 200
_superShield = 1000

class SuperSmashBro:
    """ 
    Name        :   SuperSmashBro
    Purpose     :   This class creates characters from the game "Super Smash Brothers."
    """

    # Standard constructor: to be declared when you want a constructor with parameters.
    # This gives us the ability to call the class without filling the class parameters,
    # it is useful to use because we may need to access methods in the body of SuperSmashBro class.
    def __init__(self):
        pass

    # Second constructor.
    def __init__(self, health, shield, name, isAlive):
        self.health = health
        self.sheild = shield
        self.name = name
        self.isAlive = isAlive

    def delete_brothers(load):
        """[Deletes all super smash bros.]

        Args:
            load ([type]): [The list of object to be cleared.]
        """
        for brother in range(len(load)):
            # None is our (NULL) in python.
            load[brother] = None
        return load

    # A @classmethod: Suggest that this method is only a part of this
    # class and must be accessed through a empty constructor instance
    # in order to use this method. No other classes will have access
    # to this method.
    @classmethod
    def reverse_bro_name(cls, name_of_bro):
        """[Reverses a super smash bro name.]

        Args:
            name_of_bro ([type]): [This is the name of the super smash brother.]
        
        Return:
            reversed_name
        """
        reversed_name = name_of_bro[::-1]
        return reversed_name

    # A @staticmethod: Suggest that we do not have to create
    # an object from a empty constructor we can explicitly call the
    # method as if it is not bound to the class. This allows us not
    # to have to class the method with '.' DOT notation instead we can
    # call directly.
    @staticmethod
    def display_all_brothers(list_of_brothers):
        """[Displays all super smash bros.]

        Args:
            list_of_brothers ([type]): [description]
        """
        for bro in range(len(list_of_brothers)):
            print(list_of_brothers[bro])

    # Return a readable string representation of the class object.
    def __str__(self):
        message = "\nBro name: {0}\nAlive: {1}".format(self.name, self.isAlive)
        return message

# Is this file being directly run from python or is it being imported?
if __name__ == "__main__":

    # Declare a list to store objects in a 'C' like programming approach
    super_smash_bros = []

    # This is the empty constructor call so we can have access to methods that
    # are @classmethods as well as regular methods that are NOT STATIC.
    bro = SuperSmashBro

    # Create instances of the SuperSmashBro class.
    mario = SuperSmashBro(_standardHealth, _standardShield, "Mario", _alive)
    luigi = SuperSmashBro(_standardHealth, _maxShield, "Luigi", _alive)
    bowser = SuperSmashBro(_standardHealth, _superShield, "Bowser", _alive)
    link = SuperSmashBro(_standardHealth, _maxShield, "Link", _alive)

    # Using the builtin python list functions to handle the list.
    super_smash_bros.insert(0, mario)
    super_smash_bros.insert(1, luigi)
    super_smash_bros.insert(2, bowser)
    super_smash_bros.insert(3, link)

    # This method can only be access by the class SuperSmashBro
    # collect the returned reverse word using a variable named
    # mario_in_reverse.
    mario_in_reverse = bro.reverse_bro_name(mario.name)
    luigi_in_reverse = bro.reverse_bro_name(luigi.name)
    bowser_in_reverse = bro.reverse_bro_name(bowser.name)
    link_in_reverse = bro.reverse_bro_name(link.name)

    print("[MARIO REVERSED]: " + mario_in_reverse)
    print("[LUIGI REVERSED]: " + luigi_in_reverse)
    print("[BOWSER REVERSED]: " + bowser_in_reverse)
    print("[LINK REVERSED]: " + link_in_reverse)

    # Method call: (display_all_brothers)
    bro.display_all_brothers(super_smash_bros)

    # NOTE: We do not manually have to take care of memory, but we will for fun.
    # Normally we could just use "super_smash_bros.clear()" and this will clear the
    # list empty. But I would like to make an example of a regular function one that
    # is NOT a @classmethod or @staticmethod.
    super_smash_bros = bro.delete_brothers(super_smash_bros)

    # super_smash_bros.clear(): Provides absolute clearing of the list, 
    # BUT or method will delete it and fill with a "None" marker
    # to indicate that the position is empty no-content.
    print("\nThis is the deleted list filled with (None) markers: ", super_smash_bros)
    