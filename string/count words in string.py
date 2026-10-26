s='sai siva kumar'
words=0
for i in range(len(s)):
    if s[i]!=' ':
        if i==0 or s[i-1]==' ':
            words+=1
print ('no of words = ',words)