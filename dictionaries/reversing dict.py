n=int(input('enter the elements : '))
d={}
for i in range(n):
    key=input('entert the key : ')
    value=input('entert the value :')
    d[key]=value
print('original dict: ',d)

reverse={}
for key, value in d.items():
    reverse[value]=key

print('the reversed string : ',reverse)
