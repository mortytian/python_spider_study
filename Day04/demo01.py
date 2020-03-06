"""
类
继承
多态
多继承：
    两个父类存在同名属性或方法的问题
    子类 现在本来中寻找——》父类中寻找——》超类中寻找
    父类中寻找按照继承的先后定义顺序
    子类调用父类方法 super().父类方法

重写父类方法:
    如果在子类中存在和父类同名的方法
    会覆盖父类中的同名方法

多态：
    定义时候的类型和运行时候的类型不一样，称为多态

    isinstance:判断变量是否属于某种类型

类属性和实例属性：
    类属性：类对象拥有的属性，通过类对象和实例对象都可以访问
    类属性的修改必须通过类对象
    或者实例对象通过类方法修改

类方法和静态方法
    类方法：类对象拥有的方法，需要用修饰器@classmethod标识
    对于类方法，第一个参数必须是类对象，一般是cls
    能够通过类对象和实例对象访问

    静态方法： 通过修饰器@staticmethod标识，不需要参数

    __slots__:限定实例对象随意添加属性
    只针对当前类
    子类中允许定义的属性是 父类slots与子类slots的和

    __new__
    1、至少要有一个参数cls，代表要实例化的类
    2、必须要有返回值，返回的是实例化出来的实例
        也可以返回object.__new__(cls)
    3、__init__方法有一个参数是self,self就是new方法返回的实例


单例模式：能且仅能创建一个实例


"""
class Person():
    __instance = None
    __firstInit = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__firstInit:
            self.name = name
            self.__firstInit  = True

for i in range(1,10):
    print(Person(str(i)).name)