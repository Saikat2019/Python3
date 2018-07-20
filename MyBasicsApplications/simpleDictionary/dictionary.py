import json
from difflib import get_close_matches

data=json.load(open("data.json"))
print(data)

def definition(w):
    w=w.lower()
    if w in data:
       return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),3,0.7))>0:
        yn=input("did you mean '%s' instead\n***** if YES enter Y\n***** if NO enter N\n-->" %(get_close_matches(w,data.keys(),3,0.7)[0]))
        if yn.lower()=="y":
           return data[get_close_matches(w,data.keys(),3,0.7)[0]]
        elif yn.lower()=="n":
           return "Sorry! your desired definition doesnot exist in this dictionary"
        else:
            return "please enter Y or N "
    else:
       return "\nThis word doesnot exit in this dictionary...please double check it"

word=input("\nEnter the word whose definition you want to find -> ")
output=definition(word)

if type(output)==list:
    for item in output:
        print ("# "+item)
else:
    print(output)
