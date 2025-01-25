a=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
b=[]
c=[]
d=[]
f=[]
b=list(filter(lambda x:x%2==0,a))
c=list(filter(lambda x:x%3==0,a))
d=list(filter(lambda x:x%4==0,a))
f=list(filter(lambda x:x%5==0,a))
print(b)
print(c)
print(d)
print(f)
