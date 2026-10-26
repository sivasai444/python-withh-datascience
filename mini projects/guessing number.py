import random

while True:
    user_input=int(input('enter your nubmer = '))
    computer_input=random.randint(1,10)
    if (user_input==computer_input):
        print('you guessed the correct number 😍')
        print('you won the game 👌❤️')
        break
    else:
        print('please try again')
        continue