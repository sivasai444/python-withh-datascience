# s = input("Enter a string: ")

# lst = list(s)
# result = []

# for i in range(len(lst)):
#     if lst[i] not in result:
#         result.append(lst[i])

# print("After removing duplicates:", ''.join(result))

s='saishiva'
lst=[]
res=[]

for i in range (len(s)):
    lst=lst+[s[i]]

for i in range(len(lst)):
    found=False

    for j in range(len(res)):
        if lst[i]==res[j]:
            found=True
            break

    if found==False:
        res=res+[lst[i]]

for i in range(len(res)):
    print(res[i],end=' ')

