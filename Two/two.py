"""
    [ DESCRIPTION ]: This is the second sample file
                     of python.
"""
__title__ = "Sample Two."
__author__ = "Braiden Gole"
__version__ = "1.0.0"

# Using the help of a local module to assist us in some simple operations.
from collections import Counter

food = [
    "Peppers", "Pepperoni", "Chips", "Beer", "Pop",
    "Cheese", "Lemons", "Coffee", "Milk", "Onions",
    "Olives", "Apples", "Oatmeal", "Steak", "Candy",
    "Peppers", "Chips", "Beer", "Pop", "Garlic", "Soup",
]

# Get the amount of food items
all_food_items = Counter(food);
top_five_food_items = all_food_items.most_common(5)

# top_five_food_items: most_common() returns a tuple of the quantity of
# elements at which the tuple will obtain a tuple is constant/immutable
# and can only be indexed off of, tuples are really good for performace.
print(top_five_food_items, "\n")

# Remove a few single entries from the food list.

# Create a function.
def delete_item_in_food_list(item_to_delete):
    count = 0
    for item in food:
        if (item == item_to_delete):
            count = count + 1
            food.remove(item)
    if (count > 0):
        return True
    return False

while (True):
    # Get input for our function.
    delete_what_item = input("Enter in the potential item to delete or 'x' to quit: ")
    if (delete_what_item == "x"): 
        break
    # Supply the function with the value gathered.
    is_deleted = delete_item_in_food_list(delete_what_item)
    if (is_deleted == True): 
        print("Entry Deleted !")

# Show the list with some items removed.
print(food)

