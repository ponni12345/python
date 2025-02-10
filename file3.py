name=input("enter the name:")
age=input("enter your age:")
place=input("enter your place:")
file=open("employeelist.txt","a")
file.write("\n"+name+"\t"+age+"\t"+place)

name=input("enter your name:")
place=input("enter your place:")


file=open("employeelist.txt","r")
info=file.read().split("\n")
for data in info:
    data=data.split("\t")
    if name==data[0] and place==data[2]:
        print("successfully logged in..")
        break
    else:
        print("not placed try again..")
