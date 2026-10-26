
while True:
    u1=int(input("Enter first number: "))
    u2=int(input("Enter second number: "))
    user_input=(input("Enter the operation you want to perform (+, -, *, /): "))
    if user_input=='+':
        print(f'{u1} + {u2} = {u1+u2}')
    elif user_input=='-':
        print(f'{u1} - {u2} = {u1-u2}')
    elif user_input=='*':
        print(f'{u1} * {u2} = {u1*u2}')
    elif user_input=='/':
        print(f'{u1} / {u2} = {u1/u2}')
        continue
    else:
        print('valid operator 🤦‍♂️')
        continue