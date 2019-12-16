import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.len() > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return len(self.storage)


s = Stack()
s.push(100)
s.push(101)
s.push(105)
for i in range(s.len()):
    print(f"Pop{s.pop()}")
