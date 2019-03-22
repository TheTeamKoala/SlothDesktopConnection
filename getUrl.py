import requests

import sys
#print(sys.argv[1:])



url = 'https://slothweb.herokuapp.com/'


#resp = requests.get(url=url+"/1")   # +1 eklenmeyedebilir.
#data = resp.json()

#print(data) # Check the JSON Response Content documentation below

def get(id):   # get ile id sini veya name ini bildigin bir seyi sorgulayabilirsin. get Apple veya get 1 gibi .
    if id.isdigit():
        resp = requests.get(url=url+"product"+"/"+id)   
        data = resp.json()
        print(data) 
    else:
        resp = requests.get(url=url+"product"+"/name/"+id)   
        data = resp.json()
        print(data) 

def getAll_Func():  # product table daki butun urunleri doner
    resp = requests.get(url=url+"/product")
    data = resp.json()
    print(data)

def getAll_Fridge():  # buzdolabinda olan butun urunleri doner
    resp = requests.get(url=url+"/product/fridge")
    data = resp.json()
    print(data)



if(sys.argv[1] == "get_id"):
    get(sys.argv[2])
elif(sys.argv[1]=="get_all_product"):
    getAll_Func()
elif(sys.argv[1]=="get_all_fridge"):
    getAll_Fridge()

