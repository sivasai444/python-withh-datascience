import random

choices={'r':'🪨', 'p':'📃','s':'✂️'}
emoji=('r','p','s')

while True:
    user_choice=input('emter the user choice from these (r/p/s) = ').lower()
    if user_choice not in emoji:
        print('invalid choice !')
        continue
        
    computer_choice=random.choice(emoji)
    print(f'user choice {choices[user_choice]}')
    print(f'computer choice {choices[computer_choice]}')

    if (computer_choice==user_choice):
        print('tie ! 😒')
    elif ((computer_choice=='s' and user_choice=='r') or 
          (computer_choice=='p' and user_choice=='s') or
          (computer_choice=='p' and user_choice=='r')):
        print('YOU WIN 😍')
    else:
        print('YOU LOSS')

    while True:
        user_continue = input("Do you want to continue? (y/n): ").lower()

        if user_continue == 'y':
            break
        elif user_continue == 'n':
            print("Thank you ❤️")
            quit()
        else:
            print("Please enter y or n.")
        
         
        

