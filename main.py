import pandas as pd

dictFile = open('./french_dictionary.csv','r')
translateFile = open('./t8.shakespeare.txt','r')

Lines = dictFile.readlines()
translateLine = translateFile.readlines()
french_dict = {}

for word in Lines:
    current = word.split(',')
    french_dict[current[0]] = current[1]

print(french_dict['membership'])

frequency_dict = {}

with open('t8.shakespeare.txt', 'r') as input_file:
    with open('output_file.txt', 'w') as output_file:
        count = 0
        for line in input_file:
            # count += 1

            for word in line.split():
                temp = ''.join(filter(str.isalnum, word))
                if temp.lower() in frequency_dict:
                    frequency_dict[temp.lower()] += 1
                else:
                    frequency_dict[temp.lower()] = 1
                word = ''.join(filter(str.isalnum, word))
                output_file.write(french_dict.get(word.lower(), word))
                output_file.write(' ')
            output_file.write('\n')

df = pd.DataFrame(data=frequency_dict, index=['count'])

df = (df.T)

print (df)

df.to_excel('frequency.xlsx')



