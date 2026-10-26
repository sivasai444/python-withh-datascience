s = input("Enter a sentence: ")

words = []
word = ""

# Convert sentence into words manually
for ch in s:
    if ch != " ":
        word = word + ch
    else:
        if word != "":
            words = words + [word]
            word = ""

# Add the last word
if word != "":
    words = words + [word]

# Total number of words
count = 0

for word in words:
    count = count + 1

print("Total number of words:", count)

# Find longest and shortest word
longest = words[0]
shortest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

    if len(word) < len(shortest):
        shortest = word

print("Longest word:", longest)
print("Shortest word:", shortest)

# Find frequency of each word
print("Word frequency:")

for i in range(len(words)):
    already_checked = False

    for j in range(i):
        if words[i] == words[j]:
            already_checked = True

    if already_checked == False:
        frequency = 0

        for word in words:
            if word == words[i]:
                frequency = frequency + 1

        print(words[i], ":", frequency)



# s=input('enter the string = ')
# w=s.split()
# print('no of words = ',len(w))
# print('max word = ',max(w,key=len))
# print('min words',min(w,key=len))
# print('frequency "')
# for ch in set(w):
#     print(ch,':',w.count(ch))



