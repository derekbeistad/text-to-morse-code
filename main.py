import pandas as pd
import csv

df = pd.read_csv('morse_code_chart.csv', index_col=0, header=None, quoting=csv.QUOTE_NONE, on_bad_lines='skip')
morse_dict = df.to_dict()[1]

user_input = input("Enter a string: ")
str_input = user_input.upper().upper()

encoded_phrase = ''
for char in str_input:
    if char == ',':
        code == '--..--'
    elif char in morse_dict:
        code = morse_dict[char]
    else:
        raise KeyError(f'The character "{char}" is not in our Morse Code dictionary, please try again with a different character')
    encoded_phrase += code + "  "

print(f'You entered:\n{user_input}\n\n'
      f'Your encoded message is("/" represents a space):\n{encoded_phrase}')
