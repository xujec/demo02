#
# # readline :读取行
file = open('a.txt','r')
#
# while True:
#
#     hang = file.readline()
#     if not hang:
#         break
#
#     print(hang)
#
# file.close()


# readlines:读取所有行

lines = file.readlines()

for line in lines:
    print(line)

file.close()