s='abcdcdcdc'
sub='cdc'
cnt=0
n=len(s)
m=len(sub)
for i in range(n-m+1):
    if s[i:i+m]==sub:
        cnt+=1
print(cnt)

