import os 
import multiprocessing 
 
def child_process(): 
    print("Child process running with PID:", os.getpid()) 
 
if __name__ == "__main__": 
    parent_process = multiprocessing.Process(target=child_process) 
    parent_process.start() 
    parent_process.join() 
 
file_path = "example.txt" 
with open(file_path, "w") as file: 
    file.write("Hello, World!") 
 
with open(file_path, "r") as file: 
    data = file.read() 
    print("Read from file:", data) 
 
os.chmod(file_path, 0o755)   
