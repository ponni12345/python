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
#function to print string from one to eight with a delay
def print_string():
    for str in ["one","two","three","four","five","six","seven"]:
        print(str)
        time.sleep(2)
#creating thread for the two function
thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_letters)
thread3=threading.Thread(target=print_string)
#starting the therads
thread1.start()
thread2.start()
thread3.start()
#waiting for both threads to complete
thread1.join()
thread2.join()
thread3.join()
print("both threads have finished.")

