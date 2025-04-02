from itertools import islice,starmap,tee
#custom Iterator class
class CustomIterator:
    def __init__(self,start,stop):
        self.current=start
        self.stop=stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.stop:
            val=self.current
            self.current += 1
            return val
        else:
            raise StopIteration
#using custom iterator
print("custom Iterator:")
custom_iter=CustomIterator(1,10)
for val in custom_iter:
    print(val,end=" ")
print("\n")

#using islice(0to slice an iterator
print("islice example:")
numbers=iter(range(10,21))
sliced=islice(numbers,3,7)
print(list(sliced))

#using starmap()for function mapping
print("starmp example:")
def multiply(a,b):
    return a*b
pairs=[(2,3),(4,5),(6,7)]
result=list(starmap(multiply,pairs))
print(result)

#using tee()to duplicate an iterator
print("tee example:")
original_iter=iter(range(1,6))
it1,it2=tee(original_iter,2)
print("first iterator:",list(it1))
print("second iterator:",list(it2))

#built-in iterators
print("Built-in Iterator Example:")
my_list=[10,20,30,40]
list_iterator=iter(my_list)
for item in list_iterator:
    print(item,end=" ")
print("\n")    
        
