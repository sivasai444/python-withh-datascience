s=input('enter the string = ')
result=''
for ch in s:
    if ch not in result:
        result=result+ch
print('removed duplicates=',result)


# s = input("Enter a string: ")

# result = "".join(dict.fromkeys(s))

# print("String after removing duplicates:", result)