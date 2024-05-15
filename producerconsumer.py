import threading 
import time 
import random 
 
buffer = []   
buffer_size = 5   
mutex = threading.Semaphore()   
full = threading.Semaphore()   
empty = threading.Semaphore(buffer_size)  
 
MAX_ITERATIONS = 20   
 
 
def producer(): 
    while True: 
        item = random.randint(1, 108) 
        empty.acquire() 
        mutex.acquire() 
        while len(buffer) == buffer_size: 
            print("Buffer is full. Producer is waiting.") 
            mutex.release()  
            time.sleep(1)  
            mutex.acquire()   
        buffer.append(item) 
        print(f"Produced {item}. Buffer: {buffer}") 
        mutex.release() 
        full.release() 
 
def consumer(): 
    for _ in range(MAX_ITERATIONS): 
        mutex.acquire() 
        if len(buffer) == 0: 
            print("Buffer is empty. Consumer is waiting.") 
            mutex.release()   
            time.sleep(1)   
        else: 
            item = buffer.pop(0) 
            print(f"Consumed {item}. Buffer: {buffer}") 
            mutex.release() 
            empty.release() 
 
 
producer_thread = threading.Thread(target=producer) 
consumer_thread = threading.Thread(target=consumer) 
 
 
producer_thread.start() 
consumer_thread.start() 
 
 
producer_thread.join() 
consumer_thread.join() 
