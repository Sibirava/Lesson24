from model.human import Human

class Student(Human):
    def __init__(self, name, surname, age, mark=4):
        print("constructor from Student class")
        #вызываем в этом конструкторе конструктор ближайшего базового класса
        super().__init__(name, surname, age)   #дилегирование
        self.mark = mark

    def run(self):
        print(f"Student {self.name} is running to canteen")

    def study(self):
        self.run()
        print(f"Student {self.name} is studying ")

# s1 = Student("Alex")
# print(s1.name)
# s1.run()
# s1.study()
#
# s2 = Student("Kate")
# print(s2.name)
# s2.run()
# s2.study()