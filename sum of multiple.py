print("sum of multiplication of n natural number")
print("******************************************")
n=int(input("enter n:"))
if n>0:
    sum=0
    for i in range(n*1):
        sum+=n*n-1
print("sum of multiplication of n natural numbers is:",sum)
