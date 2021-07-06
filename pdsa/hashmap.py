# Using a linkedlist for collision handling
from pdsa import linkedlist

# Define the key/value data structure
class HashData:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

# Extend the linked list structure to implement search using the key/value data structure
class HashLinkedList(linkedlist.Node):
    def search_list(self, search_key: int):
        # Step through linked list to find the key, return the value at that key
        # or return false if nothing is founkd
        node = self
        while node.next is not None:
            if node.data.key == search_key:
                return node.data.value
            node = node.next
        # Return false if nothing is found
        return False

class HashMap:
    def __init__(self, size: int = 16):
        """
            This hash map is implemented with an array of linked lists
            The linked list data is encapsulated in the HashData class
        """
        self.size = size
        self.hash_array = [HashLinkedList()] * size

    def insert(self, name: str, value: int):
        # Assuming values are strings
        key = hash(name)
        index = key % self.size
        new_data = HashData(key, value)
        # Linked List insertion of data
        self.hash_array[index].insert_begin(new_data)
    
    def lookup(self, name):
        # Look up by key
        # Return false if nothing is found
        key = hash(name)
        index = key % self.size
        return self.hash_array[index].search_list(key)
        