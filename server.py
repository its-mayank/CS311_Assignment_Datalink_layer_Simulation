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
        print("\n")
        while True:
            data = conn.recv(1024)
            temp = data.decode('utf-8')
            #print(temp)
            if not data:
                break
            #conn.sendall(data)
            print("=============================================================================")
            print("Data recieved from socket is ::\n ",temp)
            physical_decoded_output = manchester_decoding(bitarray(temp))

            print("=============================================================================")
            print("Data after manchester decoding is ::\n ",physical_decoded_output)
            #print("LEngth of message before header removing is\n",len(physical_decoded_output))
            print("=============================================================================")
            removed_header_output=remove_header(bitarray_to_string(physical_decoded_output))

            print("Data after removing header is ::\n ",removed_header_output)
            #print("LEngth of message after removing header is\n",len(removed_header_output))
            datalink_decoded_output = crcdecode(removed_header_output)

