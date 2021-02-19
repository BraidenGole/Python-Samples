"""
    [DESCRIPTION]: This is a depth tree traversal.

    In this example we will be using more of pythons very powerful
    special data methods and loop comprehension in order to achieve a
    depth tree traversal.

    When we define __iter__() in our class we are essentially creating a
    custom looping process, I elaborate on the subject in the code below.

    Now there are at least two things when it comes to creating a for loop
    or an iteration process and that would be:

    1. Loop structure (in this case contents of __iter__())
    2. Incrementing the loop, otherwise know as __next__()

    __next__() and __iter__() work together to create the looping structure.

    We will be integrating this idea in a tree traversal.
    ------------------------------------------------------------------------
    This program applies the concept of "forward declarations" which may not
    be the best practice, however it does work here is how.

    Everything is an object in python so when we define a method after
    and call it before inside of another method this is known as a "forward declared"
    function. There can be more things that are "forward declared" rather than just
    functions alone. When this situation gets executed python will execute the first method
    up until the call to the second method inside of the first method, when this occurrs
    python will fetch the "Primary Key ID" and map to the body of the nested function and
    python will execute the function from that point forth.
    -------------------------------------------------------------------------
    [NOTE]: This project was quite hard but once I understood how __iter__() and
    __next__() worked it made much more sense, all it is, is a different way of thinking that
    I am not use to making this difficult.
"""
__title__ = "Depth traversal"
__author__ = "Braiden Gole"
__version__ = "1.0.0"
__copyright__ = "Copyright 2020, Braiden Gole"

class Tree:
    """
    Name        :   Tree
    Purpose     :   This class will represent the tree in which we will fill
                    so then we can traverse the tree to find all possible nodes.
    """
    
    def __init__(self, data):
        self.data = data
        self.nodes = []

    # We are creating a two way interface to adding a node.
    # because we must first create the node then use the class
    # method to add the node to the tree.
    def add_leaf(self, sub_leaf):
        self.nodes.append(sub_leaf)

    def __iter__(self):
        return iter(self.nodes)

    def caller(self):
        return DepthTraversal(self)

    # Return a string readable representation of the class leaf.
    def __str__(self):
        return "\tLeaf = [{}]".format(self.data)

class DepthTraversal:
    """
    Name        :   DepthTraversal
    Purpose     :   This class will hold methods that will assist in the
                    depth traversal.
    """
    
    def __init__(self, root):
        self.root = root
        self.currentNode = None
        self.nestedLeaf = None

    # The reason why we must define the __iter__ method in this class
    # and return self is because "for" loops by default call iter() this
    # is why we iterators themeselves needs a separate interface/method
    # in order to get them to function separately from for loops.
    def __iter__(self):
        return self

    # We must define a next method so we can complete the custom looping structure.
    # This specifically handles how we get to the next node so we can traverse all
    # the way down the tree.
    def __next__(self):
        if (self.currentNode is None):
            self.currentNode = iter(self.root)
            return self.root
        elif (self.nestedLeaf):
            try:
                nextLeaf = next(self.nestedLeaf)
                return nextLeaf
            except StopIteration:
                self.nestedLeaf = None
                return next(self)
        else:
            self.nestedLeaf = next(self.currentNode).caller()
            return next(self)
    
if __name__ == "__main__":

    # Instantiate the class and fill the tree.
    
    # We must be careful how we will this tree because there is no
    # logic balancing the tree data so we have to ensure that each side
    # is getting filled evenly.
    treeRoot = Tree('A')

    leaf_1 = Tree('B')
    leaf_2 = Tree('C')
    leaf_3 = Tree('D')
    leaf_4 = Tree('E')
    leaf_5 = Tree('F')
    leaf_6 = Tree('G')

    # Create the next two points from the root.
    treeRoot.add_leaf(leaf_1)
    treeRoot.add_leaf(leaf_2)

    # Add some children to each of the two points
    leaf_1.add_leaf(leaf_3)
    leaf_1.add_leaf(leaf_4)

    leaf_2.add_leaf(leaf_5)
    leaf_2.add_leaf(leaf_6)

    # Use a loop to print out all nodes in tree.
    print("\n  -- All Nodes in Tree --")
    for leaves in treeRoot.caller():
        print(leaves)



