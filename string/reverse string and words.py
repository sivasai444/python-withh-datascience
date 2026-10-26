s = input("Enter a sentence: ")

# 1. Reverse the complete string
reverse_string = ""

for i in range(len(s) - 1, -1, -1):
    reverse_string = reverse_string + s[i]

print("String in reverse:", reverse_string)


# Convert sentence into words manually
words = []
word = ""

for ch in s:
    if ch != " ":
        word = word + ch
    else:
        if word != "":
            words = words + [word]
            word = ""

if word != "":
    words = words + [word]


# 2. Reverse the order of words
reverse_words = ""

for i in range(len(words) - 1, -1, -1):
    reverse_words = reverse_words + words[i] + " "

print("Words in reverse order:", reverse_words)


# 3. Reverse characters of each word
reverse_each_word = ""

for word in words:
    reverse_word = ""

    for i in range(len(word) - 1, -1, -1):
        reverse_word = reverse_word + word[i]

    reverse_each_word = reverse_each_word + reverse_word + " "

print("Each word reversed:", reverse_each_word)



# s=input('enter the sentence = ')
# # print('string in reverse',s[::-1])
# w=s.split()
# # print('words in reverse = ',' '.join(w[::-1]))
# result=[]
# for i in w:
#     result.append(i[::-1]) 
# print('the result of 3 = ',' '.join(result))
