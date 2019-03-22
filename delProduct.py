import requests

import sys



url_del_fridge = 'https://slothweb.herokuapp.com/product/update/del/' # bu url buzdolabindan urun cikarmak icin gereken url.
url_del_table = 'https://slothweb.herokuapp.com/product/del/' # product table dan urun cikarma.

name = sys.argv[2]
id = sys.argv[2]


def delete(name):  # name ile buzdolabindan urun cikarma , id ile product tabledan urun cikarma  !!!!!!!!!!!!!!CALISMIYOR
	if name.isdigit():
		resp = requests.delete(url=url_del_table+name) # name yazdigimiza aldanma , aslinda id
		#data = resp.json()
		#print(data)    # bu satirlar yorum olarak kalmali , yoksa exception verecektir.
	else:
		resp = requests.get(url=url_del_fridge+name)   # 
		#data = resp.json()
		#print(data)    # bu satirlar yorum olarak kalmali , yoksa exception verecektir.




if(sys.argv[1] == "delete"):
    delete(name)
