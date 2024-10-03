# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
import os
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

FILE = os.path.join(os.getcwd(), "day 26 NATO", "NATO-alphabet-start", "nato_phonetic_alphabet.csv")

alphabet = pandas.read_csv(FILE)
nato_dic = {row.letter:row.code for (index, row) in alphabet.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    user_word = input("NATO code translator. Enter a word: ").upper()
    try:
        word_in_nato_code = [nato_dic[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        print()
        generate_phonetic()
    else:
        print(word_in_nato_code)

generate_phonetic()