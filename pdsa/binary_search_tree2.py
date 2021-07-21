class BSTNode():
    def __init__(self, num):
        self.left_ptr = None
        self.right_ptr = None
        self.val = num

    def insert(self, num):
        if self.val >= num:
            if self.left_ptr is None:
                self.left_ptr = BSTNode(num)
            else:
                self.left_ptr.insert(num)
        elif self.val < num:
            if self.right_ptr is None:
                self.right_ptr = BSTNode(num) 
            else:
                self.right_ptr.insert(num)


    def traverse_print(self):
        if self.left_ptr is not None:
            self.left_ptr.traverse_print()
        print(self.val)
        if self.right_ptr is not None:
            self.right_ptr.traverse_print()

    def search(self, num):
        if self.val == num:
            # The number can represent a key to some more data
            return num
        elif num < self.val:
            if self.left_ptr is None:
                # Represents no found num
                return -1
            return self.left_ptr.search(num)
        else:
            if self.right_ptr is None:
                return -1
            return self.right_ptr.search(num)

    def invert(self):
        if self.right_ptr is not None:
            self.right_ptr.invert()

        if self.left_ptr is not None:
            self.left_ptr.invert()

        temp_ptr = self.right_ptr
        self.right_ptr = self.left_ptr
        self.left_ptr = temp_ptr
    
if __name__ == "__main__":
    bst = BSTNode(5)
    bst.insert(3)
    bst.insert(6)
    bst.insert(20)
    bst.insert(5)
    bst.traverse_print()
    print("Found: " + str(bst.search(5)))
    print("Found: " + str(bst.search(20)))
    bst.invert()
    print("Inverted.")
    bst.traverse_print()
    print("Inverted again")
    bst.invert()
    bst.traverse_print()