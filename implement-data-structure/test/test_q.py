from random import randint
from unittest import TestCase
from q import *


class TestQ(TestCase):

    def test_size(self):
        test_q = Q()
        test_q.push(randint(1, 100))
        self.assertEqual(test_q.size(), 1)
        test_q.push(randint(1, 100))
        self.assertEqual(test_q.size(), 2)
        n = randint(1, 10)
        for i in range(n):
            test_q.push(n)
        self.assertEqual(test_q.size(), n+2)

    def test_is_empty(self):
        test_q = Q()
        self.assertTrue(test_q.is_empty())
        n = randint(1, 10)
        for i in range(n):
            test_q.push(n)
        self.assertFalse(test_q.is_empty())

    def test_push(self):
        test_q = Q()
        for i in range(9):
            test_q.push(i)
        pop_item = str(test_q.pop())
        self.assertIn(str(i), str(test_q))

    def test_pop(self):
        test_q = Q()
        for i in range(9):
            test_q.push(i)
        pop_item = str(test_q.pop())
        self.assertNotIn(pop_item, str(test_q))

class TestItem(TestCase):
    # no functions to test
    pass