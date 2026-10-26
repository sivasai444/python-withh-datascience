class Student:
    def display(self, name, age):
        print("Name:", name)
        print("Age:", age)

    def display(self,k):
        if k%2==0:
            print('even')
        else:
            print('odd')

s1 = Student()
s1.display("Shiva", 23)
s1.even(25)