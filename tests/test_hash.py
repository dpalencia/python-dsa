import unittest 
from pdsa import hashmap

class TestHash(unittest.TestCase):
    def setUp(self):
        self.hash_map = hashmap.HashMap(24)

    def test_insert_lookup(self):
        self.hash_map.insert("Daniel Palencia", 1337)
        self.assertEqual(self.hash_map.lookup("Daniel Palencia"), 1337)
