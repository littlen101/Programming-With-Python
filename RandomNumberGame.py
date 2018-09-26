# import sys 
import random

initial_prompt = '\nPlease enter an integer between 1 & 100:  '
num_not_int = 'Entry is not an integer.\n'
wish_to_play = 'Y'

# Function returns boolean, indicating whether an entry is an int datatype with a value greater than 0.
def is_int(sInputVal):   
    try:
        int(sInputVal) > 0
        return True
    except ValueError:
        return False

while wish_to_play == 'Y' or wish_to_play == 'y':
    input('\nWelcome to The Random Number Guessing Game! Press ENTER to begin.\n')
    random_num = random.randint(1, 100)  # Integer from 1 to 100
    random_num = int(random_num)
    # print (random_num)
    num_input = input(initial_prompt)
    bNum_input_is_int = is_int(num_input)
    while num_input != random_num:
        while bNum_input_is_int is False:
            print(num_not_int)
            num_input = input(initial_prompt)
            bNum_input_is_int = is_int(num_input)
        num_input = int(num_input)    
        if num_input < random_num:
            print('Your guess is too low! Try again.\n')
            num_input = input(initial_prompt)
        elif num_input > random_num:
            print('Your guess is too high! Try again.\n')
            num_input = input(initial_prompt)
    if num_input == random_num:
        print('\nYou guessed correctly! Congratulations!')
        wish_to_play = input('\nWould you would like to play again? (Type Y and press ENTER. (Or press ENTER to exit game.)): ')
print('\nThank you for playing The Random Number Guessing Game!')





