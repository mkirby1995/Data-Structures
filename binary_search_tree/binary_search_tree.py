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


    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        arr = []
        storage = Stack()
        storage.push(node)
        while storage.len() > 0:
              target = storage.pop()
              arr.append(target.value)
              if target.left:
                  storage.push(target.left)
              if target.right:
                  storage.push(target.right)

        for i in range(len(arr)):
            for i in range(0, len(arr) - i - 1):
                a = arr[i]
                b = arr[i + 1]
                if a > b:
                    a_index = arr.index(a)
                    b_index = arr.index(b)
                    arr[a_index] = b
                    arr[b_index] = a
        for i in arr:
            print(i)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
          storage = Queue()
          # Put root in queue
          storage.enqueue(node)
          # While queue not empty
          while storage.len() > 0:
          #   Pop front from queue
              target = storage.dequeue()
          #   DO THING
              #print(target.value)
          #   if left
              if target.left:
          #       add left to back
                  storage.enqueue(target.left)
          #   if right
              if target.right:
          #       add right to back
                  storage.enqueue(target.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
          # Make a stack
          storage = Stack()
          # Put root in stack
          storage.push(node)
          # While stack not empty
          while storage.len() > 0:
          #     Pop root out of stack
                target = storage.pop()
          #     DO THING
                #print(target.value)
          #     if left
                if target.left:
          #         Add left to stack
                    storage.push(target.left)
          #     if right
                if target.right:
          #         Add right to stack
                    storage.push(target.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
