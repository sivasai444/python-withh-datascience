n=input('entr the sentence : ')
words=n.split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)
