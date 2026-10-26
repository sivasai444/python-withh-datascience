# s=input('enter the string = ')
# word=s.split()
# longest=max(word,key=len)            #key=len (it means comparing the keys(words) with their lengths)
# print(longest)

s = input("Enter a sentence: ")

word = ""
longest = ""

for i in range(len(s)):
    if s[i] != " ":
        word = word + s[i]
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

if len(word) > len(longest):
    longest = word

print("Longest word:", longest)