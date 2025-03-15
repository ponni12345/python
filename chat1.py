import threading
import queue
import time
#shared message queue
message_queue=queue.Queue()
#function to simulate a user sending message
def user_chat(user_name):
    while True:
        message=input(f"{user_name}:")
        if message.lower()=="exit":
            print(f"{user_name}left the chat.")
            break
        message_queue.put(f"{user_name}:{message}")
        time.sleep(0.5)
#function to continuously read message from the queue
def display_messages():
    while True:
        while not message_queue.empty():
            print(message_queue.get())
        time.sleep(1)
#starting message display thread
display_thread=threading.Thread(target=display_messages,daemon=True)
display_thread.start()
#creating chat user (threads)
user1=threading.Thread(target=user_chat,args=("Alice",))
user2=threading.Thread(target=user_chat,args=("Bob",))
user3=threading.Thread(target=user_chat,args=("sam",))
user4=threading.Thread(target=user_chat,args=("raj",))
#start chat user
user1.start()
user2.start()
user3.start()
user4.start()
#waiting for user to finish
user1.join()
user2.join()
user3.join()
user4.join()
print("chat ended.")
