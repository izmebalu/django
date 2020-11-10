import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apicbv'
resp = requests.get(BASE_URL+ENDPOINT) #sending request in the form of http
data = resp.json() #receiving request in json and it gets converted to dictionary
print(data)
print("Data from django application")
print('#'*20)
print("Employee Name:", data['name'] )
print("Employee Age:", data['age'] )
print("Employee Domain:", data['domain'] )
print("Employee Salary:", data['sal'] )
print("Employee Address:", data['addr'] )

