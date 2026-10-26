# s = input("Enter a string: ")

# frequency = {}

# for ch in s:
#     if ch in frequency:
#         frequency[ch] = frequency[ch] + 1
#     else:
#         frequency[ch] = 1

# print("Character frequency:")

# for ch in frequency:
#     print(ch, ":", frequency[ch])

# print("Characters occurring more than once:")

# for ch in frequency:
#     if frequency[ch] > 1:
#         print(ch)



s = input("Enter a string: ")

for ch in set(s):
    count = s.count(ch)
    print(ch, ":", count)

print("Characters occurring more than once:")

for ch in set(s):
    if s.count(ch) > 1:
        print(ch)