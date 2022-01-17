#语法格式：
# try:
#   可能出现异常的代码块
# except Exception as e:
#   print(e)

# try:
#     print(10*2/0)
#
# except Exception as e:
#     print(e)
# print("++++++++++++")


def div(x,y):
    try:
        # 可能出现异常的代码
        z = x / y
        return z

    except Exception as e:
        # 抛出异常
        print(e)



print(div(6,3))
print(div(6,0))#异常执行代码
print(div(6,12))