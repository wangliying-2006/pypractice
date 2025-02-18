#（1）封装
class Student:
    def __init__(self, name, age):
        # 公共成员变量
        self.name = name
        # 私有成员变量
        self.__age = age

    def info(self):
        print('姓名：' + self.name)
        print('年龄：' + str(self.__age))
a=Student("WANG","10")
print(a.name)#可以
#print(a.__age)#不可以
a.info()
# Student类包括了两个成员变量（name和age）和一个成员函数（info()）。
# 其中，name是公共成员变量，可以被外部访问；而age被定义成私有成员变量，只能在类内部访问。
# 通过封装，可以保证数据不被外部随意修改，保证代码的安全性。
#(2)继承
class Animal:
    def __init__(self, name):
        # 私有成员变量
        self.__name = name

    def eat(self):
        print(self.__name + '开始偷吃零食')


class Cat(Animal):
    def __init__(self, name):
        # 调用父类的构造函数
        super().__init__(name)

    def run(self):
        print(self._name + '开始逃跑')

# Animal类是一个基类，Cat类继承了Animal类的属性和方法，并且增加了一个新的方法scratch()。
# 通过继承，在Cat类中可以调用Animal类的成员函数eat()。
#（3）多态
class Animal:
    def __init__(self, name):
        # 私有成员变量
        self.__name = name

    def make_sound(self):
        # 抽象方法
        pass


class Cat(Animal):
    def __init__(self, name):
        # 调用父类的构造函数
        super().__init__(name)

    def make_sound(self):
        print(self.__name + '猫叫')


class Dog(Animal):
    def __init__(self, name):
        # 调用父类的构造函数
        super().__init__(name)

    def make_sound(self):
        print(self.__name + '狗叫')

# Animal类包含一个抽象方法make_sound()，它在子类中被重写，实现了多态。
# Cat类和Dog类都是Animal类的子类，它们重写了make_sound()方法
# 使得同一个行为（make_sound()）在不同情况下有不同的表现形式。