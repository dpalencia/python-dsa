import unittest

# Linked list implementation with just a node class
class Node:
    def __init__(self, data = None, next = None):
        self.next = None
        self.data = data

    def insert_begin(self, data):
        # Insertion to beginning in O(1) time
        
        # If there is no data in head,
        # simply insert data here.
        if data is None:
            self.data = data
        else: 
            # Move data from old head to a new node
            old_head = Node(self.data)
            old_head.next = self.next
            
            # This head node gets the new node data,
            # points to the old head
            self.next = old_head
            self.data = data

    def remove_begin(self):
        # Move node data of the next node to this head
        new_head = self.next
        self.data = new_head.data
        self.next = new_head.next


    def insert_end(self, data):
        # Inserting to the end of the linked list
        # in O(n) time
        new_node = Node(data)
        new_node.next = None
        node = self
        while node.next is not None:
            node = node.next
        node.next = new_node
    
    def remove_end(self):
        # Removing from the end of a list in O(n) time
        # Case of a 1 element list
        node = self
        if node.next is None:
            self.data = None
            return
        else:
            while node.next.next is not None:
                node = node.next
            node.next = None

    def get_data(self):
        return self.data

    def print_list(self):
        # iterate and print all data items in list
        # head to tail
        node = self
        while node is not None:
            print(node.data)
            node = node.next
            


if __name__ == "__main__":
    unittest.main()

