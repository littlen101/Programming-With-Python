# import sys 
import random

# If want to change integer range, do so here.
int_range_start = 1
int_range_stop = 100

# If want to change number of attempts allowed/remaining, do so here.
int_num_attempts_allowed = 10

initial_prompt = '\nPlease enter an integer between {} & {}:  '.format(int_range_start,int_range_stop)
num_not_int = 'Entry is not an integer between {} & {}.\n'.format(int_range_start,int_range_stop)
wish_to_play = 'Y'



# Function returns boolean, indicating whether an entry is an int datatype with a value greater than 0.
def is_int(sInputVal):   
    try:
        int(sInputVal) > 0
        return True
    except ValueError:
        return False

while wish_to_play == 'Y' or wish_to_play == 'y':
    int_num_attempts_remaining = int_num_attempts_allowed - 1
    input('\nWelcome to The Random Number Guessing Game!' 
        '\nYou will have {} attempts to guess a number correctly.'
        '\n**Press ENTER to begin.**\n'.format(int_num_attempts_allowed))
    random_num = random.randint(int_range_start, int_range_stop)  # Obtain random number within integer range
    random_num = int(random_num)
    # print (random_num)
    num_input = input(initial_prompt)
    bNum_input_is_int = is_int(num_input)
    while num_input != random_num and int_num_attempts_remaining != 0:
        while bNum_input_is_int is False or int(num_input) < int_range_start or int(num_input) > int_range_stop:
            print(num_not_int)
            num_input = input(initial_prompt)
            bNum_input_is_int = is_int(num_input)
        # while bNum_input_is_int is True and num_input != random_num: 
        num_input = int(num_input)    
        if num_input < random_num:
            print('Your guess is too low! Try again. (You have {} attempts remaining)\n'.format(int_num_attempts_remaining))
            num_input = input(initial_prompt)
        elif num_input > random_num:
            print('Your guess is too high! Try again. (You have {} attempts remaining)\n'.format(int_num_attempts_remaining))
            num_input = input(initial_prompt)
        int_num_attempts_remaining = int_num_attempts_remaining - 1
    if int_num_attempts_remaining == 0:
        print('You have run out of chances!\n')
    elif num_input == random_num:
        print('\nYou guessed correctly! Congratulations!')
    wish_to_play = input('\nWould you would like to play again? (Type Y and press ENTER. (Or press ENTER to exit game.)): ')
print('\nThank you for playing The Random Number Guessing Game!')





