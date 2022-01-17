# 导包
import unittest
# 导入测试用例
import testcase_01

from parameterized import parameterized
import testcase_02
# 调用测试套件
suite = unittest.TestSuite()
# suite.addTest(testcase_01.my_test("test_01"))
# suite.addTest(testcase_01.my_test("test_02"))
# suite.addTest(testcase_02.my_test("test_01"))



# 执行测试用例
suite.addTest(unittest.makeSuite(testcase_01.my_test1))
# suite.addTest(unittest.makeSuite(testcase_02.my_test))
runner = unittest.TextTestRunner()
runner.run(suite)


