# 1. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。


# temp = 0
# s = 0
# n = int(input('n='))
# a = int(input('a='))
#
# def my_sum(temp, s, n, a):
#
#     for x in range(n):
#         temp += a
#         a = a * 10
#
#     return s + temp
#
# print(my_sum(temp, s, n, a))








# 2. 编写程序，随机生成10以内的一个整数，如果该数字大于圆周率 π，就将其当做直径计算圆的周长
# 和面积；否则当做半径计算圆的周长和面积。最后将计算结果输出。

# import math
# import  random
#
# a = random.randint(1, 10)
# if (a > math.pi):
#     # print('2')
#     print(math.pi*(a/2)**2)
# else:
#     print('不好意思')
# 3. 创建一个数据集，包含1到10的随机整数，共计100个数。 并统计每个数字的次数。
# import  random
# lst = [range(98),random.randint(1,10)]
# print(lst)
# 4. 字符串s = ‘Life is short You need python’。统计这个字符串中每个字母出现的次数.

import pprint
s0 = 'Life is short You need python'
count = {}
for x in s0:
    # lst = []
    count.setdefault(x,0)
    count[x] += 1
    pass

pprint.pprint(count)

    # print(str.count(str1))
# 5. 写一个满足如下功能的猜数游戏：
# 计算机随机生成一个100以内的正整数；
# 用户通过键盘输入数字，猜测计算机所生成的随机数。
# 对用户的输入次数不做限制