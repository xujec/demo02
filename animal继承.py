
class animal:
    def run(self):
        print('跑')


    def eat(self):

        print('吃饭')


class dog(animal):

    def jiao(self):

        print('犬吠')
d = dog()
d.jiao()
d.eat()
d.run()