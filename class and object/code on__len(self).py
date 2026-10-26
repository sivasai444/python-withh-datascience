class Student:
    def __init__(self,name,id,age):
        self.std=name
        self.id=id
        self.age=age
    def __str__(self):
        return f'name:{self.std},id:{self.id},age:{self.age}'
    def __repr__(self):
        return f'Student(name:{self.std!r},id{self.id},age{self.age})'
    def __len__(self):
        return len(self.std)
    def show_length(self):
        return (f'std length:{len(self.std)},id:{len(str(self.id))},age:{len(str(self.age))}')
s1=Student('sai',192210057,24)
print(str(s1))
print(repr(s1))
print(len(s1))
print(s1.show_length())
