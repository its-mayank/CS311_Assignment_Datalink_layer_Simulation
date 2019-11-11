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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        s.sendall(bitarray_to_string(s_input).encode('utf-8'))
    # print('Received', repr(data))


message_to_bits = bitarray()


msg = input("Enter the message\n")
message_to_bits.frombytes(msg.encode('utf-8'))
#print(bitarray_to_string(message_to_bits))
#print(message_to_bits.tobytes().decode('utf-8'))
print(message_to_bits)
print("Enter the Ip Address of the host you want to connect!")
HOST = input()
print("Enter the Port number of the connecting PC")
PORT = input()

datalink_encoded_output = crcencode(bitarray_to_string(message_to_bits))
print("=============================================================================")
print("Output After CRC encoding is ::\n ",datalink_encoded_output)
print("=============================================================================")
#print("LEngth of message before header is\n",len(datalink_encoded_output))

header_added_output = add_header(datalink_encoded_output,PORT,HOST)

print("Output after adding header is ::\n ",header_added_output)
print("=============================================================================")
#print("Length of message after header is\n",len(header_added_output))

#print(datalink_encoded_output)
physical_encoded_output = manchester_encoding(header_added_output)
print("Output After Manchester Encoding is ::\n ",physical_encoded_output)
print("=============================================================================")

sendData(physical_encoded_output)

# print(physical_encoded_output)
# physical_decoded_output = manchester_decoding(physical_encoded_output)

# print(physical_decoded_output)
# datalink_decoded_output = crcdecode(bitarray_to_string(physical_decoded_output))