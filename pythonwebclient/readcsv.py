import csv
with open('samplecsv.csv', mode = 'r') as file:
    csvfile = csv.DictReader(file)
    for lines in csvfile:
        print(lines)
