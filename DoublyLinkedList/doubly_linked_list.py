"""
    [DESCRIPTION]: Python 3 Doubly linked-list.

    This doubly linked list will hold a bank node as if it was
    a user in a Bank Management System.
"""
__title__ = "Bank Management System"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2021, Braiden Gole"
__date__ = "2021-03-08"

import random


class BankAccountNode:
    """
    Name        :   BankAccountNode
    Purpose     :   This class represents a node for a doubly-linked
                    list algorithm.
    """

    def __init__(self, account_number, name, email):
        self.account_number = account_number
        self.name = name
        self.email = email
        self.next = None
        self.prev = None


class Accounts(BankAccountNode):
    """
    Name        :   Accounts
    Purpose     :   This class will hold methods for our doubly linked
                    list that will hold our bank accounts.
    """

    def __init__(self, account_id, name, email):
        super(Accounts, self).__init__(account_id, name, email)

    @staticmethod
    def generate_account_number():
        return str(random.randrange(1, 1000))

    # This will create a new account in the system.
    def create_account(self, head_of_list, tail_of_list):
        self.account_number = self.generate_account_number()
        self.name = input("Enter in your name: ")
        self.email = input("Enter in your email: ")

        # Did the user fill in anything?
        if self.name == "" or self.email == "":
            print("You must enter in something !")
            self.create_account(head_of_list, tail_of_list)

        # Fill the node with the writen in data.
        new_account = BankAccountNode(self.account_number, self.name, self.email)
        new_account.prev = new_account.next = None

        # Is the head of the list empty?
        if head_of_list is None:
            # If it is empty fill the head and tail that way when we traverse in reverse we
            # will have an entry to print.
            head_of_list = new_account
            tail_of_list = new_account
            return head_of_list, tail_of_list
        else:
            head_reference = head_of_list
            next_node = head_of_list.next

            # Handle insertion once we get to the proper spot.
            new_account.prev = head_reference
            new_account.next = next_node
            head_reference.next = new_account

            # Is the tail empty ?
            if next_node is None:
                tail_of_list = new_account
            else:
                next_node.prev = new_account
        return head_of_list, tail_of_list

    # This will update an account in the system.
    @staticmethod
    def update_account(head_of_list, account_name):
        while head_of_list is not None:
            if head_of_list.name == account_name:
                head_of_list.email = input("Enter in a new email: ")
            head_of_list = head_of_list.next

    # This will delete a account in the system.
    @staticmethod
    def delete_account(head_of_list, account_name):
        while head_of_list is not None:
            if head_of_list.name == account_name:
                head_of_list.name = None
                head_of_list.email = None
                return head_of_list
            head_of_list = head_of_list.next
        return head_of_list

    # This method will show all of the accounts in the system.
    @staticmethod
    def show_all_accounts(head_of_list):
        while head_of_list is not None:
            if head_of_list.name is not None or head_of_list.email is not None:
                print("Account: {" + head_of_list.account_number + "}, " + head_of_list.name + " " + head_of_list.email)
            head_of_list = head_of_list.next

    # This method will show all of the accounts in the system in reverse order.
    @staticmethod
    def show_all_accounts_names_in_reverse(tail_of_list):
        while tail_of_list is not None:
            if tail_of_list.name is not None or tail_of_list.email is not None:
                print("Account: {" + tail_of_list.account_number + "}, " + tail_of_list.name + " " + tail_of_list.email)
            tail_of_list = tail_of_list.prev


if __name__ == "__main__":

    # Create some instances.
    accounts = Accounts(None, None, None)

    head = None
    tail = None

    selection = 0
    activate_bank = True
    while activate_bank:
        try:
            print("\n-- Main Menu --")
            print("\t1. Create account")
            print("\t2. Update account")
            print("\t3. Delete account")
            print("\t4. Show all accounts")
            print("\t5. Show all accounts in reverse")
            print("\t6. Exit")

            # Gather input then check to see if it is in the proper range.
            selection = int(input("Enter in a number: "))
            if not 1 <= selection <= 6:
                print("\nOut of range, selections are from [1-6].\n")

            if selection == 1:
                head, tail = accounts.create_account(head, tail)
            elif selection == 2:
                account_to_update = input("Enter in the account name to update: ")
                accounts.update_account(head, account_to_update)
            elif selection == 3:
                account_to_delete = input("Enter in the account name to delete: ")
                head = accounts.delete_account(head, account_to_delete)
            elif selection == 4:
                accounts.show_all_accounts(head)
            elif selection == 5:
                accounts.show_all_accounts_names_in_reverse(tail)
            elif selection == 6:
                activate_bank = False
        except ValueError:
            print("\nNo characters !\n")
