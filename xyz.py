class Student:
    def greet(self):
        print("Hello", self.name)

    def __init__(self, name):
        self.name = name

student1 = Student("Sai")
student1.greet()