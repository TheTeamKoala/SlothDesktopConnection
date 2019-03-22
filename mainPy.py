import requests
import os
import sys



if(sys.argv[1] == "get_id"):
    os.system('python getUrl.py ' + sys.argv[1] + ' ' + sys.argv[2])  # burdaki argv1 "get" olacak , argv2 ise neyi getirmek istedigin.
elif(sys.argv[1]=="get_all_product"):
    os.system('python getUrl.py ' + sys.argv[1])  # burdaki argv1 getAll olacak , tek argumanli ise
elif(sys.argv[1]=="get_all_fridge"):
    os.system('python getUrl.py ' + sys.argv[1])  # burdaki argv1 getAll olacak , tek argumanli ise
elif(sys.argv[1]=="delete"):
    os.system('python delProduct.py ' + sys.argv[1] + ' ' + sys.argv[2])  # del name verirsek "Fanta" gibi fridge den siler , id verirsek tabledan siler.
elif(sys.argv[1]=="post"): # product table a urun eklemek icin , add gibi calismaz , add  isme sahip olan urunu buzdolabina ekler.
    os.system('python postProduct.py ' + sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + ' ' + sys.argv[4] + ' ' + sys.argv[5] + ' ' + sys.argv[6] + ' ' + sys.argv[7] + ' ' + sys.argv[8] + ' ' + sys.argv[9] + ' ' + sys.argv[10])
    # post icin urun icin gerekli olan 9 ozellik girilecek bosluklarla girilecek , bunun icin kodun cagrildigi yerde ufak bi methodla stringler birlestirilerek kolayca cagrilabilir.
elif(sys.argv[1]=="add"):
    os.system('python add.py ' + sys.argv[2])  # burdaki argv2 eklenmek istenen urunun name i olacak.
elif(sys.argv[1]=="post_order"):
    os.system('python postOrder.py ' + sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + ' ' + sys.argv[4] + ' ' + sys.argv[5]) # order a ait ozellikler girilecek.
elif(sys.argv[1]=="get_all_order"):
    os.system('python getOrder.py ' + sys.argv[1])  # burdaki argv1 get_all_order olacak , tek argumanli ise
elif(sys.argv[1]=="get_order"):
    os.system('python getOrder.py ' + sys.argv[1] + ' ' + sys.argv[2])  # burdaki argv1 get_order olacak , argv2 ise order id olacak.
elif(sys.argv[1]=="delete_order"):
    os.system('python deleteOrder.py ' + sys.argv[1] + ' ' + sys.argv[2])  # burdaki argv1 delete_order olacak , argv2 ise order id olacak.
else:
    print("False using")

