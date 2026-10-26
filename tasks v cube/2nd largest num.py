# list1=[12,23,1,5,45,9]
# list1.sort(reverse=True)

# print(list1[1])

l=[13,23,4,56,90,20]
larg=sec_larg=l[0]

for num in l:
    if num>larg:
        sec_larg=larg
        larg=num

    elif num>sec_larg and num!=larg:
        sec_larg=num

print('2 large number= ',sec_larg)