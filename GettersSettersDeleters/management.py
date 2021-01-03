"""
    [DESCRIPTION]: This is sample #11.

    This is a demonstration on using getters, setters, and deleters a typical
    object oriented approach to object manipulation this is a good way
    to "encapsulate" your data.

    (Assigns)
    SETTER METHODS: These methods do not return anything !
                    They only assign the class attribute when the "thing to assign"
                    is valid.

    (Retrieves)
    GETTER METHODS: This method is to retrieve the current value of a class
                    attribute. An example could be accessing the current value
                    in a display function, now that the data is encapsulized we
                    have to use a getter method which will "Return" the value.
"""
__title__ = "Sample 11"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

import sys

class CEO:
    """
    Name        :   CEO
    Puropose    :   This class represents the highest ranking corporate
                    individual in a workplace.
    """

    # Empty constructor.
    def __init__(self):
        pass

    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email

    # Getter methods.
    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email
    # End Getter methods.

    # Setter methods.
    @name.setter
    def name(self, name_to_set):
        try:
            # Use isinstance to see if we have a string for a name.
            if not isinstance(name_to_set, str):
                raise TypeError
            else:
                self._name = name_to_set
        except TypeError:
            sys.stderr.write("\n\tThe [name] is of the wrong type !")

    @last_name.setter
    def last_name(self, last_name_to_set):
        try:
            # Use isinstance to see if we have a string for a name.
            if not isinstance(last_name_to_set, str):
                raise TypeError
            else:
                self._last_name = last_name_to_set
        except TypeError:
            sys.stderr.write("\n\tThe [last_name] is of the wrong type !")

    @email.setter
    def email(self, email_to_set):
        try:
            # Use isinstance to see if we have a string for a name.
            if not isinstance(email_to_set, str):
                raise TypeError
            else:
                self._email = email_to_set
        except TypeError:
            sys.stderr.write("\n\tThe [email] is of the wrong type !")
    # End Setter methods.

    # Deleter methods.
    @name.deleter
    def name(self):
        raise AttributeError("\n\tERROR: Must keep name, cannot delete !")

    @last_name.deleter
    def last_name(self):
        raise AttributeError("\n\tERROR: Must keep last name, cannot delete !")

    # This one will actually delete !
    @email.deleter
    def email(self):
        print("\n\tEmail: [{0}] has been deleted !".format(self._email))
        del self._email
    # End Deleter methods.

    # Return a class representation of the CEO.
    def __str__(self):
        message = "CEO: {0} {1}".format(self.name, self.last_name)
        return message

if __name__ == "__main__":
    # Instantiate a ceo.
    ceo = CEO("Braiden", "Gole", "braiden_gole@gmail.com")

    # Print out the string readable representation of the ceo.
    print("\n", ceo)

    #del ceo.name
    #del ceo.last_name

    # The ceo's email is the only field that is actually allowed
    # to be deleted so it will print out a message when we do so.
    # The others will throw an AttributeError exception.
    del ceo.email
