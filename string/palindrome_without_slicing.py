# s = input("Enter a string: ")

# reverse = ''.join(reversed(s))

# if s == reverse:
#     print("Palindrome")
# else:
#     print("Not a palindrome")



s = input("Enter a string: ")

is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")