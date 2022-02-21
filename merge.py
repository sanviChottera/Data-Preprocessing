import csv

dataset1 = []
dataset2= []

with open("dataset_1.csv","r") as f:
    c = csv.reader(f)
    for i in c:
        dataset1.append(i)


with open("sorted.csv","r") as f:
    c = csv.reader(f)
    for i in c:
        dataset2.append(i)


header1 = dataset1[0]
planet_data1 = dataset1[1:]


header2 = dataset2[0]
planet_data2 = dataset2[1:]


headers = header1 + header2

planet_data = []
for index,data_row in enumerate(planet_data1):
    planet_data.append( planet_data1[index] + planet_data2[index])

with open("final.csv", "a+") as f:
    c = csv.writer(f)
    c.writerow(headers)
    c.writerows(planet_data)
