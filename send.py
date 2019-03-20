
import json
import requests
for i in range(100):
	url = "http://localhost:9200/company/employees/"+str(i)
	headers = {'content-type': "application/json"}
	payload = {"name" : "KC"+str(i),"age" : "50"+str(i)}
	r = requests.post(url, json=payload)
	print(r.text)
	print(r.json())
