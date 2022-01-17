# str = "hello world"
# print(str)

# str = "name"

#字符串的格式化

s1 = "我的名字叫%s" % "王五"
print(s1)

s2 = "我今年%d" % 25

# print(s2)
#
# s3 = "一斤苹果%f元" %  3.0
# print(s3)
#
# print("保留3位数字->'%.5f'" % 659)
# print("返回的数字宽度是8位，小数后两位，默认右对齐->'%8.2f'" % 659)
# #数字宽度8位，数
# # 字占了6位，剩余的两位被空格占用
# print("返回的数字宽度是8位，小数后两位，设置左对齐->'%-8.2f'" % 659)
# print("数字前显示+号->'%+8.2f'" % 659)
# print("数字前显示-号->'%+8.2f'" % -659)
# print("总宽度是8位，小数后两位，剩余空位用0补齐->'%08.2f'" % 659)


print("今天星期{}，张三买了{}斤苹果".format('二',3))
print("我是位置参数{0},{1}".format('hello','python'))
print("我是位置参数{1},{0}".format('hello','python'))
print("我是位置参数hello, python")
print("我是关键字参数:{x}".format(x="hello"))
