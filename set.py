#set
basket={"apple","banana","orange","kivi","apple"}
print(basket)
print('orange'in basket)
print('mango'not in basket)
a={"apple","banana","kivi"}
b={"apple","banana","orange"}
print(a)
print("letter in a but not in b",b-a,a-b)
print("both a or b",a|b)
print("letter in both a and b",a&b)
print("letter in a or b but not both",a^b)
#pop,max,min,difference
a={0,1,2,3,4}
b={2,3}
a.pop()
print(a)
a.add(5)
print(a)
print(max(a))
print(min(a))
print(a.difference(b))

      
