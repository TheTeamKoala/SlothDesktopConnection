import requests

import sys



url = 'https://slothweb.herokuapp.com/order/del/' # bu url buzdolabindan urun cikarmak icin gereken url.

id = sys.argv[2]


def delete_order():  # order id ile order delete edilmesi.
	resp = requests.delete(url=url+id) # name yazdigimiza aldanma , aslinda id
	#data = resp.json()
	#print(data)    # bu satirlar yorum olarak kalmali , yoksa exception verecektir.





if(sys.argv[1] == "delete_order"):
    delete_order()
