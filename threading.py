'''#single thread
import threading
import time
def print_number():
    for i in range(1,6):
        print(i)
        time.sleep(1)
print_number()
print_number()

thread1=threading.thread(target=print_number)
thread2=threading.thread(target=print_number)
thread2.start()
thread1.start()
'''
#multi thread

import threading
import time
#function to print number from 1 to 5 with  a delay
def print_numbers():
    for i in range(1,8):
        print(i)
        time.sleep(2)
        
#function to print letter from a to e with a delay
def print_letters():
    for char in ['a','b','c','d','e','f','g']:
        print(char)
        time.sleep(2)
#creating thread for the two function
thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_letters)

#starting the therads
thread1.start()
thread2.start()

#waiting for both threads to complete
thread1.join()
thread2.join()

print("both threads have finished.")

