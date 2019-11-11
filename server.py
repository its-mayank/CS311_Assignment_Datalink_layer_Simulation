from socket import *
from bitarray import *
from datalink import *
from physical import *

def bitarray_to_string(x):
    s=""
    for i in x:
        if i==False:
            s+="0"
        else:
            s+="1"  
        
    return s


HOST = "127.0.0.1"
PORT = 1947
hostname = gethostbyname('0.0.0.0')

#data = ""
global temp
with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((hostname, int(PORT)))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            temp = data.decode('utf-8')
            print(temp)
            if not data:
                break
            #conn.sendall(data)
            physical_decoded_output = manchester_decoding(bitarray(temp))

            print(physical_decoded_output)
            datalink_decoded_output = crcdecode(bitarray_to_string(physical_decoded_output))
