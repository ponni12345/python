import program
print(program.add(1,5))

from program import sub
print(sub(5,6))


from program import*
print(add(5,6))
print(sub(8,5))      
print(multi(12,4))
print(divi(12,5))

from program import*
choc=1
while(choc==1):
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    c=int(input("enter your choice="))
    if(c==1):
        print(add(a,b))
    elif(c==2):
        print(sub(a,b))
    else:
        print("please slect correct option")
choc=int(input("if you want cont...click 1...?"))        
 
