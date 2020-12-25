"""
    [DESCRIPTION]: This is the fourth python sample (Circular Doubly Linked List).

    Link below [PEP-8 -- Style Guide for Python Code]:
        https://www.python.org/dev/peps/pep-0008/

    PEP(Python Enhancement Proposal): for proper styling of python code.

    This is a simple implementation of a custom circular doubly linked list.
"""
__title__ = "Sample Four."
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

class Node:
    """
    Name        :   Node
    Purpose     :   This represents what an entry will hold in our circular
                    doubly linked list.
    """
    
    # Empty constructor
    def __init__(self):
        pass

    # This constructor creates the node, otherwise know as the record/entry.
    def __init__(self, name, last, email):
        self.name = name
        self.last = last
        self.email = email

        # Part of each record or entry in a Circular Doubly linked list
        # will have a previous and next pointer for each not created
        # this gives us the ability to traverse the list in reverse and
        # in regular linear order.
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    """
    Name        :   CircularDoublyLinkedList
    Purpose     :   This class will hold method that are relevant to a
                    circular doubly linked list.
    """

    # Constructor takes in no parameters so it is an empty constructor !
    # BUT we can initialize variables when the class gets called. If we
    # did not care to delcare variables here for the ends of our list
    # then we would have to create an empty constructor and use the word
    # pass in the body of the constructor.
    def __init__(self):
        self.head = None
        self.tail = None

    def create_user(self):
        """[This will create a user in our circular doubly linked list.]

        Returns:
            [True, False]: [Either the user was made successfully and we return True or False.]
        """
        users_name = input("Enter in a name: ")
        users_last_name = input("Enter in a last name: ")
        users_email = input("Enter in an email address: ")

        # Fill the node with the information.
        new_node = Node(users_name, users_last_name, users_email)

        # Is the head empty.
        if (self.head == None):
            self.head = new_node
            # If we would like to print in reverse we must fill the (tail)
            # node here that way we actually have an entry to print when 
            # we decide to print in reverse.
            self.tail = new_node

            # Fill the prev and next pointers.
            new_node.prev = self.tail
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node
    
    def update_user(self, user_to_update):
        """[This function will update a user in the circular list.]

        Args:
            user_to_update : [The user who we would like to update.]
        """
        self.head = self.tail
        while (True):
            if (self.head != None):
                if (self.head.name == user_to_update):
                    new_name = input("Update name: ")
                    new_last = input("Update last name: ")
                    new_email = input("Update email: ")
                    self.head.name = new_name
                    self.head.last = new_last
                    self.head.email = new_email
                    return True
            self.head = self.head.next
            if (self.head == self.tail):
                return False
    
    def delete_user(self, user_to_delete):
        """[This will delete a user in our circular doubly linked list.]

        Args:
            user_to_delete : [The user who we would like to delete.]
        """
        self.head = self.tail
        while (True):
            if (self.head != None):
                if (self.head.name == user_to_delete):
                    self.head.name = None
                    self.head.last = None
                    self.head.email = None
                    return True
            self.head = self.head.next
            if (self.head == self.tail):
                return False
            

    def display_users(self):
        """[This method will display all users in the circular doubly linked list.]"""
        self.head = self.tail
        while (True):
            if (self.head != None):
                print(self.head.name, self.head.last, self.head.email)
            self.head = self.head.next
            if (self.head == self.tail):
                break
    
    def cycle_through_users(self):
        """[This will allow you to cycle through the users one user at a
            time by enter a selection __eq__ to 4 then a selection __eq__ to 5
            in order to cycle to the next user.]
        """
        while (True):
            if (self.tail != None):
                print("Cycled Entry: ", self.tail.name, self.tail.last, self.tail.email)
            self.tail = self.tail.prev
            if (self.tail == self.head.prev):
                break

# Is this file being directly used by python or is it being imported.
if __name__ == "__main__":
    
    selection = 0
    keep_adding_users = True

    # Empty constructor calls.
    circDll = CircularDoublyLinkedList()

    while (keep_adding_users):
        try:
            print("\n-- CIRCULAR DOUBLY LINKED USER LIST --")
            print("1. Create user.")
            print("2. Update user.")
            print("3. Delete user.")
            print("4. Display user.")
            print("5. Cycle through single users.")
            print("6. Exit\n")
            selection = int(input("Enter in a selection: "))

            if (selection == 1):
                circDll.create_user()
            elif (selection == 2):
                update_who = input("Enter in the user to update: ")
                circDll.update_user(update_who)
            elif (selection == 3):
                delete_who = input("Enter in the user to delete: ")
                circDll.delete_user(delete_who)
            elif (selection == 4):
                circDll.display_users()
            elif (selection == 5):
                print("\n>>> To cycle through users enter a selection of equal to [4] " +
                      "then enter a selection equal to [5] to see the next cycled entry.\n")
                circDll.cycle_through_users()
            elif (selection == 6):
                break
            else:
                raise ValueError("Not in range of potential selections !")
        except ValueError:
            print("No characters !")