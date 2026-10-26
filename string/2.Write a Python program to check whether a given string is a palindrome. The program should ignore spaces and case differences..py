s = input("Enter a string: ")

# Remove spaces and convert uppercase to lowercase
cleaned = ""

for ch in s:
    if ch != " ":
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
        cleaned = cleaned + ch

# Reverse the string manually
reverse = ""

for i in range(len(cleaned) - 1, -1, -1):
    reverse = reverse + cleaned[i]

# Check palindrome
if cleaned == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")



#     s = input("Enter a string: ")

# cleaned = s.replace(" ", "").lower()

# if cleaned == cleaned[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")