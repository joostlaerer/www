import csv
f = open('./python/csvhandling/navneliste.csv')
csv_f = csv.reader(f)
print(type(csv_f))

fornavn= []
etternavn =[]

for row in csv_f:
  fornavn.append(row[0])
""" print (fornavn) """

for row in csv_f:
    etternavn.append(row[1])

fornavn3bok = (fornavn[2])

print (fornavn3bok[:3])