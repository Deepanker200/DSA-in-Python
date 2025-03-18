class Test:
    # x = 5  # Attribute 1

    # def f1():  # Attribute 2
    #     print("Hello")

    x=7

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):       #Instance object method
        print(self.a, self.b)

    @staticmethod
    def f2():
        print("Hello")


    @classmethod
    def f3(cls):
        print(cls.x)


t1 = Test(3, 4)
print(t1.a, t1.b)
t1.show()       #Instance object method
Test.f2()