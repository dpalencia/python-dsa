
class BinarySearchTree:
    def __init__(self, key):
        # Key to search by
        self.key = key
        self.left = None
        self.right = None

    
    def search(self, search_key):
        """ 
            Recursive search for a node and return it
            return None if no node is found
        """
        # Recursive traversal
        if search_key < self.key:
            if self.left is None:
                # If no match is found
                # and we reach the end of the tree, 
                # return none
                return None
            else:
                # Otherwise continue the search
                return self.left.search(search_key)
        elif search_key > self.key:
            if self.right is None:
                return None
            else: 
                return self.right.search(search_key)
        elif search_key == self.key:
            # Base case--
            # if key is found, return this node
            return self
        


    def insert(self, insert_key):
        if insert_key <= self.key:
            if self.left is None:
                self.left = BinarySearchTree(insert_key)
            else:
                self.left.insert(insert_key)
        else:
            if self.right is None:
                self.right = BinarySearchTree(insert_key)
            else:
                self.right.insert(insert_key)

    def traverse_print(self):
        """
            Traverse tree, print all members
        """
        if self.left is not None:
            self.left.traverse_print()
        print(self.key)
        if self.right is not None:
            self.right.traverse_print()
        
