class Student:
    def __init__(self,name,age):
        self.na='sai'
        self.ag=24
    def __str__(self):
        return f'name:{self.na}, age:{self.ag}'
    def __repr__(self):
        return f'student(name: {self.na!r}, age:{self.ag})'
s1=Student('sai',24)
print(repr(s1))
print(str(s1))
        