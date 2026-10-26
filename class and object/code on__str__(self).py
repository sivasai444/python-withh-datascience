class Student:
    def __init__(self,name):
        self.name='sai'
    def __str__(self):
        return self.name 
s1=Student('sai')
print(s1.name)
print(s1)
