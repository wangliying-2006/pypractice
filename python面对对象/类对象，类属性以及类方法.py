class Car(object):
    #类属性
    total_cars=0
    def __init__(self,make,model):
        self.make=make
        self.modle=model
        Car.total_cars+=1
    #实例方法
    def accelerate(self):
        print(f"一辆{self.make}的{self.modle}正在加速")
car1=Car("toyota","camry")
car2=Car("honda","accord")
#类对象可以直接调用类属性和类方法
print(Car.total_cars)
#通过类对象.实例方法(不这样用，但了解)
Car.accelerate(car1)