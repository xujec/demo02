# 1、复制 HTMLTestRunner.py 文件到项目文件夹
# 2、导入 HTMLTestRunner、unittest 包

import unittest
from HTMLTestRunner import HTMLTestRunner
# 3、生成测试套件 suite = unittest.TestLoader().discover("./", "test*.py") ；
suite = unittest.TestLoader().discover("./", "test*.py")

# 4、以只写方式打开测试报告文件 f = open("test01.html", "wb")
f = open("test01.html", "wb")
# 5、实例化 HTMLTestRunner 对象： runner = HTMLTestRunner(stream=f, title="
# 自动化测试报告", description="Chrome 浏览器")
runner = HTMLTestRunner(stream=f, title="自动化测试报告", description="Chrome 浏览器")
# 6,执行：runner.run(suite)
runner.run(suite)
# 7、关闭文件；
f.close()

