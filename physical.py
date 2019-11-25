from bitarray import *
# Utility function to encode the given message according to the manchester encoding.
def manchester_encoding(s):
    temp_bitarray = bitarray()
    for i  in range(len(s)):
        if( s[i]=='0' ):
            temp_bitarray.append(False)
            temp_bitarray.append(True)
        if(s[i]=='1'):
            temp_bitarray.append(True)
            temp_bitarray.append(False)
    return temp_bitarray

# Utility function to decode the given message according to the manchester encoding.
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



# Code for the testing of the individual utility functions written in the file!


# a = bitarray()
# a.extend([False,True,True,True,True,False,False,True])
# print(a)
# c = manchester_encoding(a)
# print(c)
# b = manchester_decoding(c)
