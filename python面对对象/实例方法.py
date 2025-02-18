class Dog:
    #类属性
    leg_num=4
    has_hair=True
    has_tail=True
    #实例方法
    def bark(self):#self代表实际调用的对象
        print("狗狂吠")
    def bite(self,person):
        print(f"狗咬{person}")
    def fetch(self):
        print("狗捡球")
alex=Dog()
alex.bite("wang")#alex传给self（固定的）;wang传给person