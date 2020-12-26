"""
    [DESCRIPTION]: This is sample file #8 for python.

    This is inheritance in python with the use of the super()
    keyword to fill the base class constructor.

    This can be really useful for multi-inheritance projects.
"""
__title__ = "Sample Eight"
__author__ = "Braiden Gole"
__version__ = "1.0.0"

class Bird:
    """
    Name        :   Bird
    Purpose     :   This is the base bird class.
    """

    def __init__(self, type_of_bird):
        self.type_of_bird = type_of_bird

    def __str__(self):
        return "The type of bird created: {0}".format(self.type_of_bird)

class Penguin(Bird):
    """
    Name        :   Penguin
    Purpose     :   This is the subclass Penguin.
    """

    # Create the constructor of the penguin class to fill
    # the parent (Bird) constructor.
    def __init__(self):
        super(Penguin, self).__init__("Penguin")

if __name__ == "__main__":

    # We have already created a readable string representation
    # of our class object so we can just print it out from here.
    penguin = Penguin()
    print(penguin)