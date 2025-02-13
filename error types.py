#syntax error
x=10
if x==10:
 print(x)

#runtime error


#name error
print(x)

'''#type error
x="100"
y=5
z=y+x'''

'''#index error
x=['raja','annamalai','balaji']
print(x[3])'''

'''#attribute error
x='nandhini'
x.reverse()'''

#logical error
def fact(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return r
print(fact(5))    
