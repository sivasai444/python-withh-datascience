n=int(input('entert the value : '))
lis=[]
for i in range(n):
    value=input('entert the list elements:')
    lis.append(value)
print('original value : ',lis)

print(list(set(lis)),'the duplicates removed set')