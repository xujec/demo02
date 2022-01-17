

import unittest

def my_sum(a, b):

    return a + b

class my_test(unittest.TestCase):

    def test_01(self):

        num = my_sum(1, 3)
        self.assertEqual(num, 4)

    def test_02(self):

        num = (3, 5)
        self.assertEqual(num, 9)
