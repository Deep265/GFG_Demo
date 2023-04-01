import csv


data = [{'link':'adab','item':'abc'}]

fields = ['link','item']

with open('test.csv','a') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    # writer.writeheader()

    writer.writerows(data)