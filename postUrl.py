import urllib.request
import json      


firstName = "Kucuk"
lastName = "lalem"

body = {'firstName': firstName, 'lastName': lastName}


urlBase = "http://omerdeneme.herokuapp.com"

myurl = urlBase + "/api/v1/customers"


req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)
