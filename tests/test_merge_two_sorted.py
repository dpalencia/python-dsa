import unittest
from pdsa import linkedlist
from pdsa.leetcode import merge_two_sorted
class TestMergeTwoSorted(unittest.TestCase):
    def test_merge_two_sorted(self):
        l1_head = linkedlist.Node(1)
        l1_head.insert_end(2)
        l1_head.insert_end(4)

        l2_head = linkedlist.Node(1)
        l2_head.insert_end(3)
        l2_head.insert_end(4)
        l1_head.print_list()
        l2_head.print_list()

        # Encapsulated iaaaan a class
        # because the exercise had it this way
        soln = merge_two_sorted.Solution()

        merged_head = soln.mergeTwoLists(l1_head, l2_head)
        merged_head.print_list()

if __name__ == "__main__":
    unittest.main()