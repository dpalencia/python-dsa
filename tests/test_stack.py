from pdsa import stackqueue
import unittest

class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = stackqueue.Stack()
        stack.push(2)
        stack.push(5)
        stack.push(10)
        self.assertEqual(stack.peek(), 10)
        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 2)
        self.assertTrue(stack.isEmpty())

    def test_queue(self):
        q = stackqueue.Queue()
        q.insert(0)
        q.insert(1)
        q.insert(2)
        self.assertEqual(q.remove(), 0)
        self.assertFalse(q.isEmpty())
        self.assertEqual(q.remove(), 1)
        self.assertEqual(q.remove(), 2)
        self.assertTrue(q.isEmpty())