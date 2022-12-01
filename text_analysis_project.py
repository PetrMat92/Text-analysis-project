"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Matějíček
email: matejicekpetr92@gmail.com
discord: Petr_Mat#1921
"""
# imports
import pandas as pd
import collections as col


# variables

# default set of texts ----->
txt_1 = """   
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. 
"""

txt_2 = """
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.
"""

txt_3 = """
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.

"""
texts = [txt_1, txt_2, txt_3]  # list of texts that can be selected by users via app_menu function

registered_users = {            # dictionary od registered users allowed to use the program
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

separator = "@──────────────────────────────────────────────────────────────────────@"  # graphic feature

selected_text = []  # global variable that stores users choice

# functions


def login_in() -> None:
    """
    log_in function performs following steps:
    1. asks users for username and password
    2. stores data in users_data dictionary
    2. checks whether data match any item in registered_users dictionary
    3. if data do not match with registered_users dictionary ---> function prints error message
    4. else ---> function prints welcome message
    --------------------------------------------
    :return: print(str)
    """
    users_data = {}
    print(separator)
    username: str = input("Please enter your username: ")
    password: str = input("Please enter your password: ")
    print(separator)
    users_data[username] = password
    for i in users_data.items():
        if i not in registered_users.items():
            print("unregistered user, terminating the program..")
            quit()
        else:
            print(f"Welcome to the app, {username}")


login_in()


def app_menu() -> list:
    """
    app_menu function performs following steps:
    1. prints information about selection of texts available for analysis
    2. stores users selection of text in the variable -----> choice
    2. checks whether users input match any item in the "texts" list
    3. if data do not match with any item in the list ---> function prints error message
    4. else --------> function stores the choice in the global variable "selected_texts"
            --------> prints the name of selected text
    --------------------------------------------
    :return: selected_text
    """
    choice = (input("Enter a number of a text you want to analyze (select nr. from 1 to 3): "))
    print(separator)
    if choice == "1":
        selected_text.append(texts[int(choice) - 1])
        print(f'You have selected txt_1. Initialize analysis....')

    elif choice == "2":
        selected_text.append(texts[int(choice) - 1])
        print(f'You have selected txt_2. Initialize analysis....')
    elif choice == "3":
        selected_text.append(texts[int(choice) - 1])
        print(f'You have selected txt_3. Initialize analysis....')
    elif not choice.isnumeric():
        print(f'You have entered nonnumerical symbol, terminating the program....')
        quit()
    else:
        print(f' Out of range choice, terminating the program....')
        quit()
    return selected_text


app_menu()


def txt_analysis() -> None:
    """
    txt_analysis function performs following steps:
    1. transforms selected text into string and split it
    2. stores the data in the local variable ---------> split_data
    3. analyses following characteristics: number of words, titlecase words, uppercase words
       lowercase words, numerical word, total sum of numerical words
    4. prints outcomes of analysis via pandas function DataFrame -------> prints table
    :return: print(table)
    """
    data = ''.join(selected_text)
    split_data = data.split()

    word_count = len(split_data)  # counts words in the text

    titlecase_words = 0  # counts titlecase words in the text
    for i in split_data:
        if i.istitle():
            titlecase_words += 1

    upper_case_words = 0  # counts uppercase words in the text
    for i in split_data:
        if i.isupper():
            upper_case_words += 1

    lower_case_words = 0  # counts lowercase words in the text
    for i in split_data:
        if i.islower():
            lower_case_words += 1

    numeric_words = 0  # counts numeric words in the text
    for i in split_data:
        if i.isnumeric():
            numeric_words += 1

    numeric_items = [i for i in split_data if i.isnumeric()]  # counts sum of al numeric words in the text
    sum_num = sum([int(i) for i in numeric_items])

    # print section
    fn_variables = {'words': word_count,  # printing section
                    'title words': titlecase_words,
                    'upper words': upper_case_words,
                    'lower words': lower_case_words,
                    'num words': numeric_words,
                    'sum of nums.': sum_num}
    table = pd.DataFrame(fn_variables, index=[''])
    print(separator)
    print(f'{table}')
    print(separator)


txt_analysis()


# noinspection PyTypeChecker
def chart() -> None:
    """
    app_menu function performs following steps:
    1. transforms selected text into string and split it
    2. calculates length of the words in the selected text --------> local variable word
    3. calculates frequency of a single word length via Counter function ------> Ordered frequency
    4. prints a final chart showing frequency via * symbol
    --------------------------------------------
    :return:
    """
    data = ''.join(selected_text)
    split_data = data.split()
    data_1 = []
    nums = []
    for word in split_data:
        if word.isalpha():
            data_1.append(word)
    for word in data_1:  # assign length of every word in the text to nums variable
        nums.append(len(word))

    frequency = col.Counter(nums)  # counts word length frequency
    ordered_fr = sorted(frequency.items())
    fr_dict = dict(ordered_fr)

    # print section
    print(f"{'LENGTH':>10} {'|':^10} {'OCCURRENCES':^20} {'|':^10} {'NUMBER':^17}")
    print(separator)
    for k, v in fr_dict.items():
        print(f"{k:>7} {'':^17} {'*' * v:<14} {v:>20}")
        print(separator)


chart()
