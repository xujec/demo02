import unittest

def my_test1(a,b):

    return a * b
    # return a + b


class my_test(unittest.TestCase):

    def test_01(self):

        print(my_test1(5,6))


    def test_02(self):

        print(my_test1(3,7))


