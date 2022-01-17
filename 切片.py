


lst5 = ['red','green','blue','black','gold','orange']
tup = ('red','green','blue','black','gold','orange')
str = ("adbcdfjffjfjf")
# print(lst5[2:88])
#
# print(tup[1:3:2])
# print(str[0:10:3])
# lst：表示列表的名称；
# start：表示切片的开始索引位置（包括该位置），此参数也可以不指定，默认为 0，也就是从列表
# 的开头进行切片；
# end：表示切片的结束索引位置（不包括该位置），如果不指定，则默认为列表的长度，注意end
# 不能超过列表的长度，否则会报错；
# step：表示切片的步长，如果 step 的值大于 1，则在进行切片操作时，会“跳跃式”的取元素。如
# 获取第2-5个元素:
print(lst5[1:5:])
# "获取第2,4,6个元素:"
print(lst5[1::2])
# "获取第1,3,5个元素:"
print(lst5[0:6:2])
print(lst5[::2])
# "获取第3个及后面的元素:"
print(lst5[2::])
# "将列表翻转："
print(lst5[::-1])