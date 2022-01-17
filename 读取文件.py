# 读取文件

# 打开文件,返回一个对象
file = open("a.txt",'a')
# 读取文件，写文件
result = file.write("hello,pythonnihao")

# for x in result:
    # print(x,end = "")
print(type(result))
# print(result)
# 关闭文件

file.close()