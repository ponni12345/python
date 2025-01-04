print("SUM OF SQUARE OF N NATURAL NUMBERS")
print("**********************************")
n=int(input('enter n:'))
if n>0:
    sum=0
    for i in range(n+1):
        sum+=i*i
    print("sum of square of n natural numbers is:",sum)    
