import json
f=open("file.json","r+")
data=json.load(f)

list=[]     
     

h =input()

def findbookbyname(_bookname):
     for i in data["books"]:
         if i["title"]==_bookname:
             print(i)
findbookbyname(h)  


def totalPaper():
    for i in data["books"]:
        if h=="pages":
           list.append(i["pages"])
    print(sum(list))
totalPaper()




