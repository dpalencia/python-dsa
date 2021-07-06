from pdsa import linkedlist
import unittest

class NodeTest(unittest.TestCase):
    def test_linked_list(self):
        linked_list = linkedlist.Node(0)
        linked_list.insert_end(1)
        linked_list.insert_end(2)
        linked_list.insert_begin(-1)
        linked_list.remove_begin()
        linked_list.remove_end()
        linked_list.print_list()
