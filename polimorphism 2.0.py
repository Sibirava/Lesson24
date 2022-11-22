class A:
    def __init__(self, name, age=16):
        # self.__value = 0
        self.name = name
        self.age = age

# print(A()._A__value)

class B(A):
    def __init__(self, name, age, mark):
        super().__init__(name, age)  #делегирование вызывается в самом начале
        # self.__value = 100
        self.mark = mark
        self.age = 20

b = B("alex", 30, 10)

print(dir(b))
print(b.__dict__)
print(vars(b))