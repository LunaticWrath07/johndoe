import threading 
import time 
 
# Shared resource 
file_name = "shared_file.txt" 
file_mutex = threading.Lock() 
readers_count = 0 
writing = False 
readers_wait = threading.Condition(file_mutex) 
writers_wait = threading.Condition(file_mutex) 
initial_content = "Initial content written by the first writer\n" 
 
def initialize_file(): 
    with open(file_name, 'w') as file: 
        file.write(initial_content) 
 
def reader1(): 
    global readers_count 
    with readers_wait: 
        while writing: 
            readers_wait.wait() 
        print("Reader 1 is waiting...") 
        readers_count += 1 
    # Reading from the file 
    with open(file_name, 'r') as file: 
        content = file.read() 
        print("Reader 1 reads:", content) 
        print("\n") 
    with readers_wait: 
        readers_count -= 1 
        if readers_count == 0: 
            writers_wait.notify() 
 
def reader2(): 
    global readers_count 
    with readers_wait: 
        while writing: 
            readers_wait.wait() 
        print("Reader 2 is waiting...\n") 
        readers_count += 1 
    # Reading from the file 
    with open(file_name, 'r') as file: 
        content = file.read() 
        print("Reader 2 reads:", content) 
        print("\n") 
    with readers_wait: 
        readers_count -= 1 
        if readers_count == 0: 
            writers_wait.notify() 
 
def reader3(): 
    global readers_count 
    with readers_wait: 
        while writing: 
            readers_wait.wait() 
        readers_count += 1 
    # Reading from the file 
    with open(file_name, 'r') as file: 
        content = file.read() 
        print("Reader 3 reads:", content) 
        print("\n") 
    with readers_wait: 
        readers_count -= 1 
        if readers_count == 0: 
            writers_wait.notify() 
 
def simultaneous_reader(reader_id): 
    global readers_count 
    with readers_wait: 
        while writing: 
            readers_wait.wait() 
        readers_count += 1 
        print(f"Reader {reader_id} is reading...") 
        if readers_count == 3: 
            # All readers have started reading 
            print("Data read by readers:") 
    # Reading from the file 
    with open(file_name, 'r') as file: 
        content = file.read() 
        print(content) 
        print("\n") 
    with readers_wait: 
        readers_count -= 1 
        if readers_count == 0: 
            writers_wait.notify() 
def writer1(): 
    global writing 
    with writers_wait: 
        while readers_count > 0 or writing: 
            writers_wait.wait() 
        writing = True 
    # Writing to the file 
    print("Writer1 is writing data to the file...") 
    with open(file_name, 'a') as file: 
        file.write("Data written by writer1\n") 
    with writers_wait: 
        writing = False 
        readers_wait.notify_all() 
 
def writer2(): 
    global writing 
    with writers_wait: 
        while readers_count > 0 or writing: 
            writers_wait.wait() 
        writing = True 
    # Writing to the file 
    print("Writer2 is writing data to the file...") 
    with open(file_name, 'a') as file: 
        file.write("Data written by writer2\n") 
     
    with writers_wait: 
        writing = False 
        readers_wait.notify_all() 
 
# Initialize the file with initial content 
initialize_file() 
 
# Test 
threads = [] 
threads.append(threading.Thread(target=writer1))   
threads.append(threading.Thread(target=reader1))   
threads.append(threading.Thread(target=writer2))   
threads.append(threading.Thread(target=reader2))   
threads.append(threading.Thread(target=reader3))   
threads.append(threading.Thread(target=simultaneous_reader, 
args=(1,)))   
threads.append(threading.Thread(target=simultaneous_reader, 
args=(2,)))   
threads.append(threading.Thread(target=simultaneous_reader, 
args=(3,)))   
 
for thread in threads: 
    thread.start() 
    time.sleep(0.7)  
 
for thread in threads: 
    thread.join()
