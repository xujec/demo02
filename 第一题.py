

# 1. 输入a,b,c,d 4个整数，计算a+b-c*d的结果
# a = int(input('请输入整数'))
# b = int(input('请输入整数'))
# c = int(input('请输入整数'))
# d = int(input('请输入整数'))
#
#
# print(a + b - c * d)


# 2. 对输入字符串的大小写翻转操作（大写变小写，小写变大写）

# a = input('请输入一个大写字母')
# print(a.lower())
# b = input('请输入一个小写字母')
# print(b.upper())


# 3. 判断一个数n能同时被3和5整除
n = input('请输入一数字整数')
if n % 3 and n % 5 == 0:
    
    print('可以被3和5整除')

else:
    print('不可以被3和5整除')


# 4. 编写一个程序，输入圆的半径，计算圆的面积
# pai = 3.14
# r = int(input('请输入圆的半径'))
# print(pai*r*r)

# 5. 利用凯撒密码将字母加密，偏移量为3
# 注：凯撒密码是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固
# 定数目进行偏移后被替换成密文。例如，当偏移量是3的时候，所有的字母A将被替换成D，B变成
# E，以此类推

# import string
# s = 'S'
# k = 'K'
# def kaisa_jiami(s,k):
#
#
# # 小写英文字母
#     lower=string.ascii_lowercase
# #大写英文字母
#     upper=string.ascii_uppercase
#
#     return lower ,upper
#
# print(kaisa_jiami(s,k))