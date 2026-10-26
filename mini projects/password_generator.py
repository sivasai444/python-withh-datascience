import random

num= ['0','1','2','3','4','5','6','7','8','9']
str_uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str_lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
special=['@','!','?','*','&','#','%','$','/','-','_','+']
characters= num+str_uppercase+str_lowercase+special
while True:
    random_password = ''.join(
        random.choice(characters) 
        for i in range(8)
        )
# uppercase = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
# print(uppercase)

    user=input('if user wants continue click y = ')
    if (user=='y'):
        print(f'the 8 characters random password = {random_password}')
        continue
    else:
        print('password enogh')
        break

