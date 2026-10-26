def del_chr(str1,str2):
    lst=list(str1)
    lst.remove(str2)
    res=" ".join(lst)
    return res
str1=input('enter str1=')
str2=input('choose deleting char from str1 = ')
print(del_chr(str1,str2))
