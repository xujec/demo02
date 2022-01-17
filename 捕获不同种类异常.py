try:
    num1 = int(input("请输入数字："))
    num2 = int(input("请输入数字："))
    print(num1 / num2)
except ValueError:
    print('请输入整数')


except ZeroDivisionError:
    print("除数不能为 0")
# except:

    # print('分母不能为零')