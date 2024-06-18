import csv
mydict = [{'branch': 'coe', 'cgpa': '9.0','name': 'Nikki','year': '2005'},
          {'branch': 'IT', 'cgpa': '8.0','name': 'Tina','year': '2003'},
          {'branch': 'cs', 'cgpa': '7.0','name': 'Reema','year': '2018'}]
#field names
fields = ['name', 'branch', 'cgpa', 'year']
filename = "university.csv"
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames = fields)
    writer.writeheader()
    writer.writerows(mydict)