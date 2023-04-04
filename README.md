# Text Analysis App Readme
This code is a Python program that performs text analysis on user-selected texts. The program requires users to log in with their username and password, and if the user is authenticated, they are allowed to select one of three texts available for analysis. Once the user has made their selection, the program performs a series of analyses on the text, including word count, title case word count, uppercase word count, lowercase word count, and numerical word count.

# Dependencies
- Pandas (https://pandas.pydata.org/) version 1.3.3
- Python version 3.x.x

#How to use
1) Ensure that the dependencies listed above are installed.
2) Run the program using a Python interpreter.
3) When prompted, enter your username and password. The program will authenticate your information and continue if it matches any item in the registered_users dictionary.
4) After successful authentication, the user is prompted to select one of the three texts for analysis.
5) Once a text is selected, the program performs the analysis, prints a summary of the results, and presents them in a table format.

#Code structure
The code consists of four main parts:

- Variables: This section includes the list of texts, a dictionary of registered users, and the separator graphic.
- Functions: This section includes three functions:
- login_in(): This function asks users for their username and password, stores the data in a dictionary, and checks whether the data match any item in the registered_users dictionary.
- app_menu(): This function presents a menu for users to select one of the three texts. If the selection is valid, the choice is stored in the global variable selected_text.
- txt_analysis(): This function performs the text analysis, including word count, title case word count, uppercase word count, lowercase word count, and numerical word count. The analysis is presented in a table format.
- Main program: This section includes the main program code that calls the login_in(), app_menu(), and txt_analysis() functions.

# Limitations
- The program currently only supports three pre-defined texts. It can be extended to allow users to input their texts.
- The program currently does not have any visualizations or graphs.
- The program is limited to analyzing one text at a time.
