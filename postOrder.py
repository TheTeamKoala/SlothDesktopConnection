import urllib.request
import json      
import sys

id = sys.argv[2]
date= sys.argv[3]
quantity = sys.argv[4]
product_ID = sys.argv[5]


# order ekleme kodu. command argument olarak gelen ozellikler ile order  ekler.

body = {'id': id, 'date': date , 'quantity': quantity , 'product_ID': product_ID }


urlBase = "https://slothweb.herokuapp.com/order"

myurl = urlBase


req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
