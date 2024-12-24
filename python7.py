#string concatentation
a="hello"
b="world"
c="cup"
d=a+b+c
print(d)
a="hello"
b="world"
c=a+""+b
print(c)
age=36
txt="my name is john,and i am {}"
print(txt.format(age))
print("********************")
quantity=3
itemno=567
price=49.95
myorder="i want {} pieces ofitem {} for {} dollars"
print(myorder)
print(myorder.format(quantity,itemno,price))
print("**********************")
quality=3
itemno=567
price=49.95
myorder="Iwant to pay {2} dollers for {0}\"pieces\" of item{1}"
print(myorder.format(quantity,itemno,price))
print("*******************")
a="hello,woeld"
print(a.split("l"))
