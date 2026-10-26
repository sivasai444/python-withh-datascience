#1.Write a Python program to count the number of characters, words, spaces, vowels, 
# consonants, digits, uppercase characters, lowercase characters, and special characters in a string.

# s=input('enter the string = ')

# chars=0
# words=0
# spaces=0
# vowels=0
# cons=0
# digi=0
# upper=0
# lower=0
# spl=0
# if_word=False

# for ch in s:
#     chars=chars+1


#     if ch==' ':
#         spaces=spaces+1
#         if_word=False
#     else:
#         if if_word==False:
#             words=words+1
#             if_word=True
    

#         if ch in 'aeiouAEIOU':
#             vowels=vowels+1

#         elif ch>='a' and ch<='z':
#             lower=lower+1
#             cons=cons+1

#         elif ch>='A' and ch<='Z':
#             upper=upper+1
#             cons=cons+1

#         elif ch >= '0' and ch<='9':
#             digi=digi+1

#         else:
#             spl=+1
# print('no.of chars = ',chars)
# print('no.of cons = ',cons)
# print('no.of digits = ',digi)
# print('no.of upper case = ',upper)
# print('no.of lower case = ',lower)
# print('no.of vowels = ',vowels)
# print('no.of words = ',words)
# print('no.of spaces = ',spaces)
# print('no.of special = ',spl)



s = input("Enter a string: ")
characters = len(s)
words = len(s.split())

spaces = s.count(" ")

vowels = 0
consonants = 0
digits = 0
uppercase = 0
lowercase = 0
special = 0

for ch in s:

    if ch.lower() in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    if ch.isdigit():
        digits += 1

    if ch.isupper():
        uppercase += 1

    if ch.islower():
        lowercase += 1

    if not ch.isalnum() and ch != " ":
        special += 1

print("Characters:", characters)
print("Words:", words)
print("Spaces:", spaces)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Special characters:", special)



    






  
