# s = input("Enter a string: ")

# alphabets = True
# digits = True
# alphanumeric = True
# uppercase = True
# lowercase = True
# whitespace = True

# if s == "":
#     alphabets = False
#     digits = False
#     alphanumeric = False
#     uppercase = False
#     lowercase = False
#     whitespace = False

# for ch in s:

#     # Check alphabet
#     if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z')):
#         alphabets = False

#     # Check digit
#     if not ('0' <= ch <= '9'):
#         digits = False

#     # Check alphanumeric
#     if not (('A' <= ch <= 'Z') or
#             ('a' <= ch <= 'z') or
#             ('0' <= ch <= '9')):
#         alphanumeric = False

#     # Check uppercase
#     if not ('A' <= ch <= 'Z'):
#         uppercase = False

#     # Check lowercase
#     if not ('a' <= ch <= 'z'):
#         lowercase = False

#     # Check whitespace
#     if not (ch == ' ' or ch == '\t' or ch == '\n'):
#         whitespace = False

# print("Only alphabets:", alphabets)
# print("Only digits:", digits)
# print("Alphanumeric:", alphanumeric)
# print("Uppercase:", uppercase)
# print("Lowercase:", lowercase)
# print("Whitespace:", whitespace)



s = input("Enter a string: ")

print("Only alphabets:", s.isalpha())
print("Only digits:", s.isdigit())
print("Alphanumeric:", s.isalnum())
print("Uppercase:", s.isupper())
print("Lowercase:", s.islower())
print("Whitespace:", s.isspace())