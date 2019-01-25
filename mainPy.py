import requests
import os
import sys



url = 'http://omerdeneme.herokuapp.com/api/v1/customers'


if(sys.argv[1] == "get"):
    os.system('python getUrl.py ' + sys.argv[1] + ' ' + sys.argv[2])
elif(sys.argv[1]=="getAll"):
    os.system('python getUrl.py ' + sys.argv[1])
elif(sys.argv[1]=="post"):
    os.system('python postUrl.py ' + sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3])
elif(sys.argv[1]=="update"):
    print("update")
elif(sys.argv[1]=="delete"):
    print("delete")
else:
    print("False using")

print(sys.argv[1])
print("lale")
