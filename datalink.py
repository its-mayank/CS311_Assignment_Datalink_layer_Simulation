import numpy as np
from bitarray import bitarray
from physical import *

# Utility function to convert Bitarray to String
def bitarray_to_string(x):
    s = ""
    for i in x:
        if i == False:
            s += "0"
        else:
            s += "1"

    return s

#Utility function to take XOR of 2 number i.e. a and b.
def xor(a, b): 
    result = [] 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
  
    return ''.join(result)

# Utility function to calculate the modulus-2-division for the given parameters.
def modulus_2_division(divident, divisor): 
    pick = len(divisor)  
    tmp = divident[0 : pick] 
  
    while pick < len(divident): 
  
        if tmp[0] == '1': 
            tmp = xor(divisor, tmp) + divident[pick] 
  
        else:
            tmp = xor('0'*pick, tmp) + divident[pick] 
        pick += 1

    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp) 
  
    checkword = tmp 
    return checkword 

# Function to convert the given bits into their respective integers in the base 2.
def bit_to_int(x):
    m=int(0)
    for i in x:
        m=2*m+int(i)

    return m

# Utility function that adds the header information on the bits
def add_header(msg,port,ip):
    
    port_to_bits=bitarray()
    ip_to_bits=bitarray()
    
   
    port_to_bits.frombytes(port.encode('utf-8'))
    # print(len(port_to_bits))
    ip_to_bits.frombytes(ip.encode('utf-8'))
    #print(len(ip_to_bits))
    final_mssg=None
    final_mssg=bitarray_to_string(ip_to_bits)+bitarray_to_string(port_to_bits)+msg
    #print(len(final_mssg))

    return final_mssg

# Utility function that removes the header information on the bits
def remove_header(msg):
    s=""

    for i in range(32+96,len(msg)):
        s+=msg[i]

    return s

# Utility function that encodes the message according to the CRC Encoding with 10101 as its generator function.
def crcencode(bits):
    
    m="10101"
    r="0000"
    bits+=r
    div = bit_to_int(bits)

    divd = bit_to_int(m)

    rem=modulus_2_division(bits,m)
    reminder=bit_to_int(rem)
    msg=bit_to_int(bits)
    f=int(input("Enter 1 if you want to generate error else enter 0 (This is only for testing purpose of the error detection mechanism)\n"))
    if f==1:
        return np.binary_repr(msg+reminder+1)
    else:
        return np.binary_repr(msg+reminder)    

    
# Utility function that decodes the message according to the CRC Encoding with 10101 as its generator function.
def crcdecode(msg):
    if int(modulus_2_division(msg,"10101"))==0:
        print("=============================================================================")
        print("No Error found\nMessage is:::::::")
        message="0"
        for i in range(len(msg)-4):
            message+=msg[i]
        print(bitarray(message).tobytes().decode('utf-8')) 
        return 0   
    else:
        print("=============================================================================")
        print("Error Detected! Please correct it.\n")
        return 1
    


    
