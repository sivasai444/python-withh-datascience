#Write a program to print the first 5 characters of:
#text = "PythonProgramming"
# text = "PythonProgramming"
# res=text[:6]
# print(res)


#Write a program to print the last 4 characters of:
# text = "ComputerScience"
# res=text[-4:]
# print(res)


#Print the characters from index 2 to index 7.
# text = "ABCDEFGHIJK"
# res=text[2:8]
# print(res)


#Remove the first and last character
# text = "Programming"
# res=text[1:-1]
# print(res)


#extract the word (take out the exact word we need)
# text = "I love Python programming"
# e=input('enter the word to extarct = ')
# while True:
#     if e in text:
#         print(e)
#         break
#     else:
#         print('invalid')
#         break
              
            #(OR)with slicing
# text = "I love Python programming"
# r=text[7:13]
# print(r)



#print every second character
# text = "ABCDEFGHIJKLMN"
# r=text[::2]
# print(r)
# output=ACEGIKM



#print every third character
# text = "PythonProgramming"
# r=text[::3]
# print(r)
# uotput=PhPgmn


#Print the characters at alternate positions.(1 after 1)
# text = "COMPUTER"
# r=text[::2]
# print(r)
# o/p=CMUE


#Print characters at odd indexes.
# text = "COMPUTER"
# r=text[1::2]
# print(r)
# o/p=OPTR


#Print characters at even indexes.
# text = "ABCDEFGHIJ"
# r=text[::2]
# print(r)
# o/p=ACEGI


#Reverse the string using slicing.
# text = "COMPUTER"
# r=text[::-1]
# print(r)
# o/p=RETUPMOC


#reverese a word
# word = "COMPUTER"
# r=word[::-1]
# print(r)
#RTPO

#Print the characters in reverse order, taking every second character.
# text = "ABCDEFGHIJ"
# r=text[::-2]
# print(r)
#JHFDB

#Print the characters in reverse order with a stride of 3.
# text = "ABCDEFGHIJKLM"
# r=text[::-3]
# print(r)
#MJGDA


#extract date
# date = "23-09-2026"
# r=date[:2]
# print(r)
# #23


#16. Extract an email username
# email = "student@gmail.com"
# r=email.index('@')
# print(email[:r ])
# student


#17. Extract the domain
# email = "student@gmail.com"
# r=email[7:]
# print(r)
# @gmail.com


#18. Mask a phone number
# phone = "9876543210"
# r=''
# for i in range(len(phone)):
#     if i<4:
#         r=r+phone[i]
#     else:
#         r=r+'*'
# print(r)
#9876******

#OR
# phone = "9876543210"
# r=phone[:4]+'*'*6
# print(r)
#9876******


#Extract the middle
#text = "ABCDEFGHIJ"
# r=len(text)
# res=r//2
# m=text[res]
# print(m)

# r=text[3:7]
# print(r)


#Remove the first 3 characters and the last 3 characters using slicing.
# text = "PythonProgramming"
# r=text[3:-3]
# print(r)


#Using slicing, check whether the word is a palindrome.
# t=input('enter the string = ')
# r=t[::-1]
# if r==t:
#     print('palindrome')
# else:
#     print('not palindrome')


#checking reverse
# t=input('enter the string = ')
# r=t[::-1]
# print('original: ',t)
# print('reverse: ',r)



#username from email
# email='pvsk89705@gmail.com'
# p=email.index('@')
# print(email[:p])



