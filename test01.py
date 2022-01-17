

import unittest
from parameterized import parameterized

def my_sum(a,b):

    return a + b

class testAdd(unittest.TestCase):

    @parameterized.expand([1,1,1],[2,2,4],[4,4,8])
    def test_01(self, x, y, expect):
        result = my_sum(x, y)
        self.assertEqual(result, expect)




    # def test_01(self):
    #
    #     num = my_sum(3,4)
    #     self.assertEqual(num,7)
    #
    #
    # def test_02(self):
    #
    #     num = my_sum(3,7)
    #     self.assertEqual(num,10)
    #
    # def test_03(self):
    #     num = my_sum(3, 17)
    #     self.assertEqual(num, 20)



