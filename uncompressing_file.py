import json
with open('zip.json', 'r') as file:
    words_dictionary = json.load(file)
print(words_dictionary)

with open('unzip.txt', 'w') as file:
    for i in words_dictionary['file']:
        if i != '*':
            unzipped_word = list(words_dictionary.keys())[list(words_dictionary.values()).index(int(i))]
            file.write(unzipped_word)
        else:
            file.write('\n')

