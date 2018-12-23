# import socket programming library 
import socket 
import subprocess
import sys 
  
from thread import *
import threading 
  
print_lock = threading.Lock() 
  
def threaded(c): 
    while True: 
  
        data = c.recv(4096) 
        if not data: 
              
            print_lock.release() 
            break
  
 	p = subprocess.check_output(data,shell =True) 
        c.send(p) 
  
    c.close() 
  
  
def Main(): 
    host = sys.argv[1] 
  
    port = int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
  
    s.listen(5) 
    print("socket is listening") 
  
    while True: 
  
        c, addr = s.accept() 
  
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
