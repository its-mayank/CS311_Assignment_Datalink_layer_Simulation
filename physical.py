from bitarray import *

packet_size = 8


def manchester_encoding(s):
    temp_bitarray = bitarray()
    for i  in range(len(s)):
        if( s[i]==0 ):
            temp_bitarray.append(False)
            temp_bitarray.append(True)
        if(s[i]==1):
            temp_bitarray.append(True)
            temp_bitarray.append(False)
    
    return temp_bitarray

def manchester_decoding(temp):
    temp_bitarray = bitarray()
    i=0
    while i<=(len(temp)-1):
        if temp[i] ==1 and temp[i+1]==0:
            temp_bitarray.append(True)
        if temp[i] == 0 and temp[i+1] == 1:
            temp_bitarray.append(False)
        i = i+2
   
    return temp_bitarray
