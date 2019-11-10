import socket

# def sendData():
#     print("Enter the Ip Address of the host you want to connect!")
#     HOST = input()
#     print("Enter the Port number of the connecting PC")
#     PORT = input()
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST, int(PORT)))
#         s.sendall(b'Hello, world')
#         data = s.recv(1024)

#     print('Received', repr(data))

from bitarray import *
from datalink import *
from physical import *
import socket


def bitarray_to_string(x):
    s = ""
    for i in x:
        if i == False:
            s += "0"
        else:
            s += "1"

    return s


def sendData(s_input):
    print("Enter the Ip Address of the host you want to connect!")
    HOST = input()
    print("Enter the Port number of the connecting PC")
    PORT = input()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        print(s_input)
        s.sendall(bitarray_to_string(s_input).encode('utf-8'))
    # print('Received', repr(data))


message_to_bits = bitarray()


msg = input("Enter the message\n")
message_to_bits.frombytes(msg.encode('utf-8'))
#print(bitarray_to_string(message_to_bits))
#print(message_to_bits.tobytes().decode('utf-8'))
ip = "172.17.0.0"
host = "1947"
print(message_to_bits)
datalink_encoded_output = crcencode(bitarray_to_string(message_to_bits))

print(datalink_encoded_output)
physical_encoded_output = manchester_encoding(datalink_encoded_output)

sendData(physical_encoded_output)

# print(physical_encoded_output)
# physical_decoded_output = manchester_decoding(physical_encoded_output)

# print(physical_decoded_output)
# datalink_decoded_output = crcdecode(bitarray_to_string(physical_decoded_output))
