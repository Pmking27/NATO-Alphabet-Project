import pandas as pd

data=pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dist={value.letter:value.code for (key,value) in data.iterrows()}

user_name=input("Enter your name = ").upper()

output_list=[phonetic_dist[letter]for letter in user_name]
print(output_list)