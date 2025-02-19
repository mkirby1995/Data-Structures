import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.storage = {}
        self.size = 0


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage.keys():
            node = self.storage[key]
            self.dll.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #Check and see if key in cache
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.dll.move_to_end(node)
            return

        # Check len if at limit, delete last
        if self.size == self.limit:
            del self.storage[self.dll.head.value[0]]
            self.dll.remove_from_head()
            self.size -= 1

        #if it is move to front and update value
        # if not add to the front
        self.dll.add_to_tail((key, value))
        self.storage[key] = self.dll.tail
        self.size += 1
