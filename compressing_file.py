import re
words_dictionary = dict()
words_dictionary['file'] = ''
assigned_number = 1
with open(r'test.txt', 'r') as file:
    for line in file:
        word_list = re.split(' ', line)
        for word in word_list:
            if word not in words_dictionary.keys():
                words_dictionary[word] = assigned_number
                words_dictionary['file'] += str(assigned_number)
                assigned_number += 1
            else:
                words_dictionary['file'] += str(words_dictionary[word])

            
print(words_dictionary)



        
        