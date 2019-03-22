import requests

import sys
#print(sys.argv[1:])



url = 'https://slothweb.herokuapp.com/product/update/add/'   

resp = requests.get(url=url+sys.argv[1])   # isme sahip urunu buzdolabina ekler. kisaca product table a urun eklidir ancak kalmamistir , onu eklemis oluruz
#data = resp.json()
#print(data) # 



