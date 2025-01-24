def reverse(n):
    rev=0
    while(n>0):
        r=n%10
        rev=(rev*10)+r
        n=n//10
    return rev
print(reverse(123))

n=123
a=reverse(n)
print(a)

def square(b):
    return b*b
print(square(2))
