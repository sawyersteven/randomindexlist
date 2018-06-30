import unittest
from RandomIndexList import *


class TestRandomIndexList(unittest.TestCase):

    def test_create_empty(self):
        self.assertEqual(RandomIndexList(), [])

    def test_create_random(self):
        ril = RandomIndexList(range(5, 10))
        self.assertEqual(ril[ril.index], 5)

    def test_create_specific(self):
        ril = RandomIndexList(range(5, 10), index=5)
        self.assertEqual(ril[5], 5)

    def test_get_item(self):
        ril = RandomIndexList(range(5, 10), index=5)
        self.assertEqual(ril[5], 5)
        self.assertEqual(ril[9], 9)

        ril = RandomIndexList(range(5, 10))
        self.assertEqual(ril[ril.index], 5)
        self.assertEqual(ril[ril.index + 4], 9)

    def test_get_slice(self):
        ril = RandomIndexList(range(5, 10), index=5)
        self.assertEqual(ril[5:8], [5, 6, 7])

        ril = RandomIndexList(range(5, 10))
        self.assertEqual(ril[ril.index:ril.index + 3], [5, 6, 7])

    def test_negative_index(self):
        self.assertRaises(NegativeIndexError, RandomIndexList, index=-5)

    def test_invalid_index(self):
        self.assertRaises(NonIntegerIndex, RandomIndexList, index="string")
        self.assertRaises(NonIntegerIndex, RandomIndexList, index=[])
        self.assertRaises(NonIntegerIndex, RandomIndexList, index=3.14)

if __name__ == '__main__':
    unittest.main()
