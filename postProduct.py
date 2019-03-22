import urllib.request
import json      
import sys

inTheFridge = sys.argv[2]
idd = sys.argv[3]
name = sys.argv[4]
brand = sys.argv[5]
category = sys.argv[6]
price = sys.argv[7]
price_UNIT = sys.argv[8]
physical_UNIT = sys.argv[9]
first_DATE = sys.argv[10]


# product table a urun ekleme. tum ozellikler burda sys.argv olarak aliniyor ve ekleniyor.

body = {'inTheFridge': inTheFridge, 'id': idd , 'name': name , 'brand': brand , 'category': category , 'price': price, 'price_UNIT': price_UNIT , 'physical_UNIT': physical_UNIT,'first_DATE': first_DATE}


urlBase = "https://slothweb.herokuapp.com/product"

myurl = urlBase


req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
