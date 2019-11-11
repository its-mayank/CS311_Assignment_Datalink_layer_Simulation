from bitarray import *
from datalink import *
from physical import *
import socket


def bitarray_to_string(x):
    s=""
    for i in x:
        if i==False:
            s+="0"
        else:
            s+="1"  
        
    return s


def sendData(s_input):
    print("Enter the Ip Address of the host you want to connect!")
    HOST = input()
    print("Enter the Port number of the connecting PC")
    PORT = input()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        s.sendall(s_input)
        data = s.recv(1024)
    print('Received', repr(data))


message_to_bits=bitarray()



msg=input("Enter the message\n")
message_to_bits.frombytes(msg.encode('utf-8'))
#print(bitarray_to_string(message_to_bits))
#print(message_to_bits.tobytes().decode('utf-8'))
print(message_to_bits)
datalink_encoded_output = crcencode(bitarray_to_string(message_to_bits))

print(datalink_encoded_output)
physical_encoded_output = manchester_encoding(datalink_encoded_output)

sendData(physical_encoded_output)