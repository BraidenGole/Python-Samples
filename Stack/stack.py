"""
    [DESCRIPTION]: Python 3 Stack Implementation.
"""
__title__ = "Stack"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"
__date__ = "2021-03-11"


class Stack:
    """
    Name        :   Stack
    Purpose     :   This class holds methods that help with the
                    operations of a stack.
    """

    def __init__(self, size_of_stack):
        self.size_of_stack = size_of_stack
        self.top = -1
        self.stack = []

    # Adds an item.
    def push_data(self, number):
        is_filled = self.is_full()
        if is_filled is True:
            return None
        try:
            self.top = self.top + 1
            self.stack.insert(self.top, number)
            return self.stack
        except AttributeError:
            return

    # Deletes an item.
    def pop_data(self):
        is_completely_empty = self.is_empty()
        if is_completely_empty is True:
            return -1
        # Last in first out (LIFO)
        self.stack.remove(self.peek())
        self.top = self.top - 1
        return self.stack

    # Displays the peek of the stack.
    def peek(self):
        try:
            peek_of_stack = self.stack[self.top]
            return peek_of_stack
        except TypeError:
            return

    # Displays the stack.
    def show(self):
        if self.is_empty() is True:
            return -1
        print("\n-- Stack --")
        try:
            length = len(self.stack)
            for items in range(0, length):
                if self.stack[items] != 0:
                    print(self.stack[items])
        except TypeError:
            return

    # Checks the stack to see if it is empty.
    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def is_full(self):
        if self.top == self.size_of_stack - 1:
            return True
        return False


if __name__ == "__main__":

    _size_of_stack = 10
    stack_op = Stack(_size_of_stack)

    selection = 0

    data = ""
    fill_stack = True
    while fill_stack:
        try:
            print("-- Main menu --")
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
            print("4. Show")
            print("5. Quit")
            selection = int(input("Enter in a selection: "))
            if selection == 1:
                data = input("Enter in a number: ")
                stack_op.stack = stack_op.push_data(data)
                if stack_op.stack is None:
                    break
            elif selection == 2:
                stack_op.stack = stack_op.pop_data()
            elif selection == 3:
                print(stack_op.peek())
            elif selection == 4:
                stack_op.show()
            elif selection == 5:
                break
        except ValueError:
            print("No characters, try again !")