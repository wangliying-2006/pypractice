class Dog:
    #类属性
    leg_num=4
    has_hair=True
    has_tail=True
    #方法
    def bark(self):
        print("狗狂吠")
    def bite(self):
        print("狗咬人")
    def fetch(self):
        print("狗捡球")
alex=Dog()
peiQi=Dog()
#实例属性赋值：实例对象.属性=值 向实例空间写入或修改属性和值
alex.name="lijie"
alex.age=10
print(alex.age)
#实例对象.变量 查询顺序【实例空间，类空间，父类空间】
alex.bark=1000
#此时无法调用alex.bark()
peiQi.bark()#不影响
