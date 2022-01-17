class user:
    def __init__(self):
        self.name = '姓名'
        self.sex = 'man'
        self.__pw = '123456'

    def show_name(self):
        print('tom')

    def __pwd(self):
        print('我的密码')


u = user()
u.show_name
print(u.sex)
# u.__pwd()