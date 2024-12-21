import csv

a = []
with open('Datasets/enjoysport.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)

num_of_attr = len(a[0]) - 1
print("\nThe most general hypothesis is: ", ['?'] * num_of_attr)
print("The most Specific hypothesis is: ", ['0'] * num_of_attr)

hypothesis = a[0][:-1]   # Take all columns in the first column.
print("\nFind S : Finding a maximally specific Hypothesis\n")

for i in range(len(a)):
    if a[i][num_of_attr] == 'Yes':
        for j in range(num_of_attr):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
    print('Training Example : ', i + 1, '\nHypothesis is: ', hypothesis)

print("\nThe Maximally Specific hypothesis for training set is: ", hypothesis)

