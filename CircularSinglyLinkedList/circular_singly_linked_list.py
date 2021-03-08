"""
    [DESCRIPTION]: Python 3 Circular Singly Linked List.
"""
__title__ = "Circular Singly Linked List"
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

class CircularSingly:
    """
    Name        :   CircularSingly
    Purpose     :   This class will hold methods that will assist
                    us with our circular list.
    """

    # This method creates a node to add to the list.
    @staticmethod
    def create(head, tail, value):
        new_node = Node(value)
        tail = Node(None)

        new_node.next = head
        if head is None:
            head = new_node
            tail = new_node
        else:
            new_node.next = head
            tail.next = new_node
            head = new_node
        return head

    # This method updates a node in the list.
    @staticmethod
    def update(head, item, replacement):
        if head is None:
            return None
        else:
            while head.data is not item:
                head = head.next
            if head is None:
                pass
            else:
                head.data = replacement

    # This method deletes a node in the list.
    @staticmethod
    def delete(head, item):
        head_reference = head
        while head_reference is not None:
            if head_reference.data is item:
                head_reference.data = None
                return True
            head_reference = head_reference.next
            if head_reference is head:
                return False

    # Outputs the circular singly linked list.
    def __str__(self, head):
        head_reference = head
        while head_reference is not None:
            print(head_reference.data)
            head_reference = head_reference.next
            if head_reference is head:
                break

if __name__ == "__main__":

    circ_list = CircularSingly()

    head = None
    tail = None

    head = circ_list.create(head, tail, 'A')
    head = circ_list.create(head, tail, 'B')
    head = circ_list.create(head, tail, 'C')
    head = circ_list.create(head, tail, 'D')
    head = circ_list.create(head, tail, 'E')

    #circ_list.update(head, 'D', 'Z')
    #circ_list.delete(head, 'E')

    circ_list.__str__(head)