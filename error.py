'''try:
    n=input("enter thevalue:")
    a=int(n)
    z=10/a
    print(a)
except TypeError:
    print("it has type error")
except ValueError:
    print("it has type error")
except:
    print("this has error")
print("***********************")'''


try:
    print(x)
except:
    print("an error occurred")
    
try:
    print(c)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")

try:
    x=5
    print(x)
except:
    print("something went wrong")
else:
    print("nothing went wrong")

try:
    x=5
    print(x)
except:
    print("somthing went wrong")
finally:
    print("the'try except' is finished")
