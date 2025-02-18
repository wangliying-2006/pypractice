class Person:
    total_persons = 0

    def __init__(self, name):
        self.name = name
        Person.total_persons += 1

    @classmethod
    def show_total_persons(cls):
        print("Total persons: ", cls.total_persons)


p1 = Person("Tom")
p2 = Person("Jerry")
Person.show_total_persons()