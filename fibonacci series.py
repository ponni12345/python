print("generate the fibonacci series")
print("*****************************")
n=int(input("enter the value of n:"))
f1=-1
f2=1
i=1
if n<=0:
    print("input only positive number")
else:
    print("fibonacci series is")
while i<=n:
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3
    i=i+1
