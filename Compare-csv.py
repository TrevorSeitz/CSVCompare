import sys
import collections
import csv





# load both files into separate dataframes
# file1 = pd.read_csv(input("File1 (including.csv):"), sep=';', encoding='UTF-8')
# file2 = pd.read_csv(input("File2 (including.csv):"), sep=';', encoding='UTF-8')
file1 = pd.read_csv('Parugus-live-sites.csv', sep=';', encoding='UTF-8')
file2 = pd.read_csv('SaaS-Paragus-Teams.csv', sep=';', encoding='UTF-8')
inSaas = []
notInSaas = []

for i in file2
    if i in file1
        inSaas.append(i)
    else:
        notInSaas.append(i)

open('notInTeams.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    print('hello')
    wr.write(notInSaas)

print("Not in SaaS: " notInSaas)


# f = open('notInTeams.csv', 'w', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     print(myfile)
#     wr.write(notInSaas)
# f.close()