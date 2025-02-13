print("error handling")
print("addition")
l1=[10,20,30]
try:
    a=l1[0]+l1[3]
    print(a)
except Indexoutofbound:
    print("index not in range")
finally:
    print("now in finally block")
print("try error finaly completed")    
