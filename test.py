import unittest
from pylist import List, ListItem

class SingleCases(unittest.TestCase):
    """ Test edge cases """
    def setUp(self):
        self.l = List()
        self.l.append('test_item')

    def test_one_item_head(self):
        self.l.pop()
        self.assertEqual(self.l.head, None)

    def test_one_item_tail(self):
        self.l.pop()
        self.assertEqual(self.l.tail, None)

    def test_pop_value(self):
        self.assertEqual(self.l.pop(), 'test_item')

class DoubleCases(unittest.TestCase):
    """ Test edge cases """
    def setUp(self):
        self.l = List()
        self.l.append('test_item')
        self.l.append('second')

    def test_head_equals_tail(self):
        self.l.pop()
        self.assertEqual(self.l.head, self.l.tail) 

class NumbersTestCase(unittest.TestCase):
    """ Test different numbers cases """
    def setUp(self):
        self.integers = [5, 6, -8, 0, 3, 2, -1]
        self.l = List()
        for num in self.integers:
            self.l.append(num)

    def test_integers(self):
        index = 0
        while self.l.length > 0:
            self.assertEqual(self.l.pop(), self.integers[index])
            index += 1

    def test_list_to_list(self):
        self.assertEqual(self.l.as_python_list(), self.integers)

if __name__ == '__main__':
    unittest.main()
