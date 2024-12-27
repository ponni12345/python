fruits=["orange","apple","pear"]
fruits1=["banana","kiwi","apple","banana"]

print(fruits)
print(type(fruits))

fruits.append("apple")
print(fruits)

fruits.extend(fruits1)
print(fruits)

fruits.insert(3,"mango")
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.pop()
print(fruits)

print(fruits.index("apple",2))

print(fruits.count("apple"))

fruits.sort()
print("sorted:",fruits)

fruits.reverse()
print("reverse list:",fruits)
