import pandas as pd

nato_alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet_dict = {row.letter:row.code for (index,row) in nato_alphabet_data.iterrows()}

def create_phonetic_code(name):
    try:
        name_list = [letter for letter in name]
        phonetic_code = [nato_alphabet_dict[letter.upper()] for letter in name_list if letter != " "]

    except KeyError:
        print("Sorry, the name should contain only letters and blank spaces.")
        name = input("Enter your name: ")
        create_phonetic_code(name)
    else:
        print(phonetic_code)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter your name: ")
create_phonetic_code(name)
