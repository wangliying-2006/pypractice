from tkinter.font import names


class Dog:
    #类属性
    leg_num=4
    has_hair=True
    has_tail=True
    #方法
    #类实例化步骤
    #（1）开辟实例空间
    #（2）调用__init___(实例空间地址)
    #（3）将实例空间地址作为类的实例子化的返回值
    def __init__(self,name,breed,color,age):
        print("1")
        self.name=name
        self.breed=breed
        self.color=color
        self.age=age

    def bark(self):
        print("狗狂吠")
    def bite(self):
        print("狗咬人")
    def fetch(self):
        print("狗捡球")
alex=Dog("kang","斗牛犬","黄色",10)#实例化初始化一行搞定