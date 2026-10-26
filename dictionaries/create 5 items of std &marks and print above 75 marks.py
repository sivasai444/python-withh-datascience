dict1=int(input('enter the count of elements : '))
n={}
for _ in range(dict1):
    keys=input('entert the student name: ')
    value=int(input('enatre the marks of student: '))
    n[keys]=value
print('original dict is :',n)
result={}
for peru,mark in n.items():
    if mark>=75:
        result[peru]=mark
print('students who got above 75 : ', result)
   