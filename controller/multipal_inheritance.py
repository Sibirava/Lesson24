class A1:
    def hello(self):
        print("A1")

class A2:
    def hello(self):
        print("A2")

class A3:
    def hello(self):
        print("A3")

class B(A1, A2, A3):
    pass

b = B()
print(b.mro())  #в каком порядке вызывается наследование
b.hello()
print(b)
