from bitarray import *
from datalink import *
from physical import *
import socket

# Utility function to convert the standard bitarray into string
def bitarray_to_string(x):
    s = ""
    for i in x:
        if i == False:
            s += "0"
        else:
            s += "1"

    return s

# Function which sends the input message to the Server
def sendData(s_input):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        s.sendall(bitarray_to_string(s_input).encode('utf-8'))
    # print('Received', repr(data))



print("Enter the Ip Address of the host you want to connect!")
HOST = input()
print("Enter the Port number of the connecting PC")
PORT = input()

while True:
    msg = input("Enter the message\n")
    print("mssg is ",msg)
    message_to_bits = bitarray()
    message_to_bits.frombytes(msg.encode('utf-8'))
    datalink_encoded_output=None
    datalink_encoded_output = crcencode(bitarray_to_string(message_to_bits))
    print("=============================================================================")
    #print("LEngth of message before header is\n",len(datalink_encoded_output))
    print("Output After CRC encoding is ::\n ",datalink_encoded_output)
    print("=============================================================================")
    
    header_added_output=None
    header_added_output = add_header(datalink_encoded_output,PORT,HOST)

    # print("Length of message after header is\n",len(header_added_output))
    # print("Output after adding header is ::\n ",header_added_output)
    print("=============================================================================")
    

    print(datalink_encoded_output)
    physical_encoded_output=None
    
    physical_encoded_output = manchester_encoding(header_added_output)
    print("Output After Manchester Encoding is ::\n ",physical_encoded_output)
    print("=============================================================================")
    
    i = 0
    print("Packets are:::::")
    num_packets = (int(len(physical_encoded_output)/16)-1)*16
    flag = '01111110'
    while i <= num_packets:
        temp_string = physical_encoded_output[i:i+16]
        print(flag+bitarray_to_string(temp_string)+flag)
        i = i + 16
        
    msg = None
    
    sendData(physical_encoded_output)