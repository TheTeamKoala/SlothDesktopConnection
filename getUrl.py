import requests

url = 'http://omerdeneme.herokuapp.com/api/v1/customers'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

resp = requests.get(url=url+"/1")   # +1 eklenmeyedebilir.
data = resp.json()

print(data) # Check the JSON Response Content documentation below



