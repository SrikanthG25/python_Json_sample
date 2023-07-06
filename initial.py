print("Hello this is our first application")

import json
from difflib import get_close_matches
file=json.load(open("mobile.json"))
user=input("Enter data : ")
def data(s):
    s=s.lower()   
    if s in file:
        return file[s]
    elif len(get_close_matches(s,file.keys())) > 0:
        ch = input("did u mean %s , Enter Y for Yes, N for No : " %get_close_matches(s,file.keys())[0])
        if ch == "Y" or "y":
            return file[get_close_matches(s,file.keys())[0]]
        elif ch == "N" or "n":
            return "The keyword doesnot match pls given valid"
        else:
            return "Error"
    else:
        return "The keyword doesnot match"
res=(data(user)) 
if type(res)== list:
    for i in res:
        print(i)
else:
    print(res)