import csv

import json
import requests

url = "http://localhost:9200/company/employees/1"
headers = {'content-type': "application/json"}

with open('accidents_2017.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
#            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
	    print(f'Processed {line_count} lines.')
	    payload = {row[0]}
	    r = requests.post(url, json=payload)
	    print(r.text)
            print(r.json())
