class Number:
    def __init__(self,value):
        self.n1=value
    # def __str__(self):
    #     return f'name :-{self.name}, age:-{self.age}'
    # def __repr__(self):
    #     return f'Student(name:-{self.name!r},age:-{self.age})'
    # def __len__(self):
    #     return len(self.name)
    def __add__(self, other):
        return self.n1+other.n1
n1=Number(34)
n2=Number(22)
print(n1+n2)