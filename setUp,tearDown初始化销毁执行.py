import unittest

def my_test1(a,b):

    return a * b


class my_test(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print("setUPClass 执行")
    #

    #
    @classmethod
    def setUpClass(cls):
        print('setupclass被执行')
    @classmethod

    def tearDownClass(cls):
        print('teardownclass被执行')
    def setUp(self):
        print('setUp执行')

    def tearDown(self):
        print('tearDown被执行')

    def test_01(self):

        print(my_test1(5,6))


    def test_02(self):

        print(my_test1(3,7))


