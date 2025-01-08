#nested loops
adj=['red','big','tasty']
fruits=['apple','banana','cherry']

for x in adj:
    for y in fruits:
        print(x,y)
        
#list in for loop
lists=[[1,2,3],[4,5,6],[7,8,9]]
for I in lists:
     for x in I:
         print(x)
         
#continus statement
fruits=['apple','banana','cherry']
for x in fruits:
    if x=='banana':
        continue
    print(x)

    
#increase value 3
for x in range(2, 30, 2):
    print(x)

    
#pass statement
for x in range(7):
    pass
                
        
        
         
