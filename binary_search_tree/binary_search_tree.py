import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    # Insert the given value into the tree
    def insert(self, value):
        # if inserting we must already have a root
        if self.value == None:
            #print("No root")
            return None
        # if value is < self.value go left, make a new tree if empty, otherwise
        # keep goung recurse
        elif value < self.value:
            if self.left == None:
                #print(f"No left node inserting {value}")
                self.left = BinarySearchTree(value)
            else:
                #print(f"{value} is less than {self.value}, moving left")
                self.left.insert(value)
        # if >= then go right make a new tree if empty otherwise
        # keep going recurse
        elif value >= self.value:
            if self.right == None:
                #print(f"No right node inserting {value}")
                self.right = BinarySearchTree(value)
            else:
                #print(f"{value} is greater or equal to {self.value}, moving right")
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            #print(f"{self.value} equals {target}")
            return True
        elif target < self.value and self.left != None:
            #print(f"{target} is < {self.value}, moving left")
            self.left.contains(target)
        elif target > self.value and self.right != None:
            #print(f"{target} is > {self.value}, moving right")
            self.right.contains(target)
        else:
            #print(f"{target} not found")
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            #print(f"Moving right to {self.right.value}")
            return self.right.get_max()
        else:
            #print(f"Max value found {self.value}")
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value != None:
          #print(self.value)
          cb(self.value)
          if self.right != None:
            self.right.for_each(cb)
          if self.left != None:
            self.left.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # Make a queue
        # Put root in queue
        # While queue not empty
        #    Pop front from queue
        #    DO THING
        #    if left
        #        add left to back
        #    if right
        #        add right to back


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # Make a stack
        # Put root in stack
        # While stack not empty
        #     Pop root out of stack
        #     DO THING
        #     if left
        #         Add left to stack
        #     if right
        #         Add right to stack

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
