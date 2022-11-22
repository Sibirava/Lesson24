class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

        print("constructor from Human class")

    def run(self):
        print(f"Human {self.name} is running ")