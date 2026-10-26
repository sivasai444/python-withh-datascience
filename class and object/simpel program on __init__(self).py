class Student:
    def __init__(self):
        self.a='sai'
        self.b=23
    def mobile(self,name,model):
        print('mobile: ',name)
        print('model: ',model)
s=Student()
print(s.a)
print(s.b)
s.mobile('oneplus','nord ce 2 lite')