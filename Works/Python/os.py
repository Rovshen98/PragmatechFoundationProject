import shutil
import os
list=[]
def createFileOnDesktop():
    with open(r"C:\Users\user\Desktop\firon.txt","w") as f:
        f.write("salam")


def findFileByName():
    files=os.listdir("C://")
    x=input()
    for file in files:
        if file.startswith(x):
            list.append(file)
            
        else:
            pass
    print(len(list))  
            
def copyFileToDesktop(): 
    os.chdir(r"C:\Users\user\Desktop") 
    os.mkdir("CopiedFiles") 
    f=input() 
    dst_dir=("CopiedFiles")
    shutil.copy(f,dst_dir)

while True:
    n=input("Nömrə daxil edin:")
    if int(n)==1:
        createFileOnDesktop()
    elif int(n)==2:
        findFileByName()
    elif int(n)==3:
        copyFileToDesktop()
        break