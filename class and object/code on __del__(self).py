class Student:
    def __init__(self, name):
        self.name = name
        print("Object created")

    def __del__(self):
        print("Object is being destroyed")


s1 = Student("Sai")

del s1

print("Program continues")