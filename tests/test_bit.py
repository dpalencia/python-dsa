import unittest
from pdsa import binary_index

class TestBinaryIndex(unittest.TestCase):
    def test_sum(self):
        input_array = [0,1,2,3,4,5,6,7,8]
        bit = binary_index.BIT(input_array)
        bit_sum = bit.sum(5)
        print(bit_sum)
        self.assertEqual(bit_sum,10)

