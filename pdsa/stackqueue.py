import unittest
# Implement a stack and a queue, using unit tests to run & test
# Can improve these by adding error handling
class Stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        popped = self.stack[-1] # slicing last element
        self.stack.pop() # removes last element
        return popped

    def push(self, n):
        self.stack.append(n)

    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, n):
        self.queue.append(n)

    def remove(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0



if __name__ == "__main__":
    unittest.main()


