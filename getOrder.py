import requests

import sys
#print(sys.argv[1:])



url = 'https://slothweb.herokuapp.com/order'


def get_all_order():   # butun orderlari doner
    resp = requests.get(url=url) 
    data = resp.json()
    print(data) 


def get_order():  # id sini verdigin orderi doner.
    id= sys.argv[2]
    resp = requests.get(url=url+"/"+id)
    data = resp.json()
    print(data)




if(sys.argv[1] == "get_all_order"):
    get_all_order()
elif(sys.argv[1] == "get_order"):
    get_order()

