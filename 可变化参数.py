#
#
# # 可变化参数指的是参数的数量可以变化，比如可以传递一个参数 ，2个参数，甚至更多。
#
# # 可变化参数类型有两种：
# # 接收列表形式的可变化参数，调用时，跟位置参数一样；接收字典类的参数，调用时，跟关键字参数一样
# # 那么可变化参数和位置参数 最大的不同就是 传递的参数 数量不受限制。
# def add(*args):
#
#     print(args)
#     val = sum(args)
#     return val
#     return args
# # print(add(2))
# print(add(2,3))
# print(add(2,3,4))
# print(add(2,3,7,87,1,9*1))
# print(add('python','world'))
# #可变化参数 添加列表 和元组时 需要在列表和元组前加上 *
# print(add(*['python','java1']))
# print(add(*('python','java2')))
#
# # 可变化参数，输入参数后 展示的元素方式 是以元组的形式展示
# #还有一种可变化参数 接收字典元素时，在函数中以**表示
#
# def show_info(**kwargs):
#     print(kwargs)
#
# show_info(key1 = 'python',key2 = 'hello')
#
# # 此函数同样能接收多个位置参数，但是传入的形式需要以关键字形式传递
#
# def show_info(**kwargs):
#
#     return kwargs
#
# print(show_info())
# print(show_info(key1 = 'hello'))
# print(show_info(key2 = 'hello',key3 = 'woeld'))
# print(show_info(**{'key1':'hello','key2':'woeld','key3':'woeld','key4':'woeld'}))


# 位置参数与可变参数一起使用

def add(a,b,*args):
    for x in args:

        print(x)

        sum = 0
        sum += x
        # print(sum)

    return a + b + sum
print(add(1,2,4,4,5))