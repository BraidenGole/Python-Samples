"""
    [DESCRIPTION]: Python 3 linked list.

    Another implementation of a linked list just trying to get
    a better handle on the python language.
"""
__title__ = ""
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"
__date__ = "2021-03-08"

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "{0}".format(self.data)

class LinkedList:
    """
    Name        :   LinkedList
    Purpose     :   This class will hold methods that will help
                    manage the incoming data.
    """

    # Adds a node to the list.
    def __add__(self, head, data):
        new_node = Node(data)
        new_node.next = None
        if head is None:
            head = new_node
            return head
        else:
            new_node.next = head
            head = new_node
        return head

    # Updates a node in the list.
    @staticmethod
    def update(head, item, replacement):
        while head is not None:
            if head.data is item:
                head.data = replacement
                return True
            head = head.next
        return False

    # Deletes a node in the list.
    def __delete__(self, head, instance):
        while head is not None:
            if head.data is instance:
                head.data = None
                return True
            head = head.next
        return False

    # A string readable representation of our class obj.
    def __str__(self, head):
        while head is not None:
            print(head.data)
            head = head.next

if __name__ == "__main__":

    linked_list = LinkedList()

    head = None
    head = linked_list.__add__(head, "A")
    head = linked_list.__add__(head, "B")
    head = linked_list.__add__(head, "C")
    head = linked_list.__add__(head, "D")
    head = linked_list.__add__(head, "E")

    #linked_list.update(head, "B", "Z")

    #linked_list.__delete__(head, "E")

    # Output the linked list.
    linked_list.__str__(head)
