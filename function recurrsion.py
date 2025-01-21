#function recurrsion
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=5
print("the factorial of",num,"is", factorial(num))

#lambda_function
def x(a):
    return a+10
print(x(5))

x=lambda a:a+10
print(x(5))

x=lambda a, b :a * b
print(x(5,6))
