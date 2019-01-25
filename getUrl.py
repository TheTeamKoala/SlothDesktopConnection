import requests

import sys
print(sys.argv[1:])



url = 'http://omerdeneme.herokuapp.com/api/v1/customers'


#resp = requests.get(url=url+"/1")   # +1 eklenmeyedebilir.
#data = resp.json()

#print(data) # Check the JSON Response Content documentation below

def get_Func(id):
    resp = requests.get(url=url+"/"+id)   # +1 eklenmeyedebilir.
    data = resp.json()
    print(data) # Check the JSON Response Content documentation below

def getAll_Func():
    resp = requests.get(url=url)
    data = resp.json()
    print(data)



if(sys.argv[1] == "get"):
    get_Func(sys.argv[2])
elif(sys.argv[1]=="getAll"):
    getAll_Func()


