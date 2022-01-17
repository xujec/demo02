# 定义一个程序员类

class coder:

    def __init__(self):
        self.name = '张胜男'
        self.sex = '男'
        self.age = 28


    def work(self):

        print('work')



    def sleep(self):

        print('sleep')


# 创建一个对象 自动调用init方法
c = coder()
# print(c.sleep())
# c.work()
print(c.name)
print(c.age)


