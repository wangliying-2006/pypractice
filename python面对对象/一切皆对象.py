l=list((1,2,3))
l.append(4)
print(l)
d=dict({"k1":"e"})
c=d.get("k1")
print(c)
class Dog:
    #类属性
    leg_num=4
    has_hair=True
    has_tail=True

    def __init__(self,name,breed,color,age):
        print("1")
        self.name=name
        self.breed=breed
        self.color=color
        self.age=age
alex = Dog("kang", "斗牛犬", "黄色", 10)
#(1)任何一个实例对象都属于本身类型
print(alex)
print(type(alex))
#(2)自定义类型对象属于可变数据类型
alex.age=11
print(alex.age)
#(3)实例对象也是一等公民：
# 变量传递
x=alex
alex.age=100
print(x.age)
#作为函数参数，作为函数返回值
def foo(m):
    print(m)
    print(type(m))
    m.append(4)
a=[1,2,3]
foo(a)
print(a)