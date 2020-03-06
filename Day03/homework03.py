class Human():
    def __init__(self, name, age):
        self.__name = name
        self.__age  = age
        self.__skill = []
        self.__money = 0

    def __add_skill(self, skill):
        self.__skill.append(skill)

    def __add_money(self, money):
        self.__money += money

    def sub_money(self, money):
        self.__money -= money

    def get_name(self):
        return self.__name

    def teach(self, student, skill):
        print(self.__name + ' 教 ' + student.get_name() + ' 学 ' + skill)
        student.__add_skill(skill)

    def work(self, money):
        print(self.__name + ' 工作赚钱 ' + str(money) + ' 元')
        self.__add_money(money)

    def borrow_from(self, p1, money):
        print(self.__name + ' 向 ' + p1.get_name() + ' 借钱 ' + str(money))
        self.__add_money(money)
        p1.sub_money(money)

    def show_info(self):
        print(str(self.__age) + ' 岁的 ' + self.__name + ' 有钱 ' + str(self.__money) + ' 元,它学会的技能是',end = ' ')
        for i in self.__skill:
            print(i,end = ' ')
        print()


p1 = Human('张三',35)
p2 = Human('李四',15)
p2.teach(p1,'王者荣耀')
p1.work(1000)
p1.teach(p2, 'python')
p2.borrow_from(p1, 200)
p1.show_info()
p2.show_info()