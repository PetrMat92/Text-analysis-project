"""
Bulls&cows.py: druhý projekt do Engeto Online Python Akademie
author: Petr Matějíček
email: matejicekpetr92@gmail.com
discord: Petr_Mat#1921
"""
# imports
import random
from timeit import default_timer as timer
import datetime as dt
from pyfiglet import Figlet

# global variables

separator = 36 * "──"
# functions


def welcome_message() -> None:
    """
        welcome_message function performs following steps:
        1. prints "Bulls and Cows" header
        2. prints instructions
        :return: None
        """
    f = Figlet(font='slant')
    print(f.renderText('Bulls and Cows '))
    print(f'Instructions: '
          f'\n{separator}'
          f'\n 1. Your task is to guess a secret number '
          f'\n 2. The number to be guessed is a 4 digit number'
          f'\n 3. Secret number comprises of unique digits ranging from 0 - 9'
          f'\n 4. First digit cannot start with 0'
          f'\n 5. Bulls indicate the number of correct digits in the correct position'
          f'\n 6. Cows indicates the number of correct digits in the wrong position.'
          f'\n{separator}')


def random_number_generator() -> str:
    """
    random_number_generator function performs following steps:
    1. initiates while cyclus to generate unique 4-digit number in the range of 0 to 9
    2. initiates while cyclus to ensure that 0 is not on the first index of number
    3. converts variable number to string and stores the value in variable code
    :return: code
    """
    number = []
    while len(number) < 4:
        x = random.randrange(0, 9)  # generates unique random numbers and appends them to "number" list
        if x not in number:
            number.append(x)
    while number[0] == 0:  # shuffles the code until a zero is not on the first digit position
        random.shuffle(number)

    code = ''.join(str(x) for x in number)
    return code


def game_round() -> str:
    """
    game_round function performs following steps:
    1. initializes while cycle
    2. gets guess from user
    3. if the input has 4-digits and if the input is numerical ---> function stores data in "guess" variable
    4. else ---> prints following user message: You must insert 4 digit number. Try again!
    4.      ---> new cycle
    :return: guess
    """
    while True:
        guess = input(f'{separator} \nEnter a number: ')
        if len(guess) == 4 and guess.isnumeric() and guess[0] != "0" and len(set(guess)) == 4:
            return guess
        elif guess[0] == "0":
            print(f'{separator} '
                  f'\n---> {guess}'
                  f'\nSecret number cannot start with 0, Try again!!!')
        elif len(set(guess)) < 4:
            print(f'{separator} '
                  f'\n---> {guess}'
                  f'\nYour guess must contain 4 unique digits. Try again!!!')
        else:
            print(f'{separator} '
                  f'\n---> {guess} '
                  f'\nYou must insert 4 unique digits. Try again!!!')


def game_analysis(guess, code) -> tuple:
    """
        game_analysis function performs following steps:
        1. sets up two variables (bull, cow) and assigns them the value of zero
        2. compares individual digits stored in the guess and code arguments
        3. If the digits are the same, the function increases the value of the bull variable by one
        4. If the digits are not the same, but the guess digit is on another position in code,
           ---> function increases the value of cow by one
        :return: bull, cow
        """
    bull = 0
    cow = 0
    for i in range(len(guess)):
        if guess[i] == code[i]:
            bull += 1
    for i in range(len(guess)):
        if guess[i] != code[i] and guess[i] in code:
            cow += 1
    return bull, cow


def main() -> None:
    """
       main function performs following steps:
    0. ---> calls welcome_message function that prints logo and instructions
        1. loads the "code" value from the appropriate function
          1.1 prints a welcome message
          1.2 presents the rules
          1.3 starts the countdown
          1.4 sets up empty list called "guess_list"
       2. initializes while cycle
          2.1 loads "guess" value from appropriate function
          2.2 stores every guess to guess_list variable
          2.3 loads  cow, bull value from appropriate function
          2.4 if guess is equal to code ---> function prints congratulation message to user
                                        ---> function stops counting time
                                        ---> prints the total time needed to guess the code
                                        ---> prints total number of attempts and all numbers inserted by user
          2.5 if guess is not equal to code ---> function prints numbers of bulls and cows
       :return: None
       """
    welcome_message()
    code = random_number_generator()
    print(f"Lets start with your first guess!!!")
    print(f"For testing. Code is: {code}")  # prints code for testing
    guess_list = []  # list of users guesses
    start = timer()  # starts counting time
    while True:
        guess = game_round()  # imports data from game_round function
        guess_list.append(guess)
        bull, cow = game_analysis(guess, code)  # imports data from game analysis function

        if guess == code:
            end = timer()  # stops counting time
            print(f"{separator} \n---> {guess} \nYour have won! ||"
                  f" Time: {dt.timedelta(seconds=end - start)} (hh:mm:ss.ms) ||"
                  f" Attempts: {len(guess_list)}")
            print(f'{separator} '
                  f'\nYou can find the history of your valid attempts below: '
                  f'\n{"-" * 70}')
            print("\n".join([" ".join(guess_list[i:i + 14]) for i in range(0, len(guess_list), 5)]))
            break
        if guess != code:
            if bull == 1 and cow == 1:
                print(f'{separator} \n'
                      f'---> {guess} \n'
                      f'{bull} bull, {cow} cow')
            elif bull == 1 and cow != 1:
                print(f'{separator} \n'
                      f'---> {guess} \n'
                      f'{bull} bull, {cow} cows')
            elif bull != 1 and cow == 1:
                print(f'{separator} '
                      f'\n---> {guess} '
                      f'\n{bull} bulls, {cow} cow')
            else:
                print(f'{separator} '
                      f'\n---> {guess} '
                      f'\n{bull} bulls, {cow} cows')


if __name__ == '__main__':
    main()
