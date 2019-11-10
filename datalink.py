import numpy as np
from bitarray import bitarray


def xor(a, b): 
    result = [] 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
  
    return ''.join(result)


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

def bit_to_int(x):
    m=int(0)
    for i in x:
        m=2*m+int(i)

    return m


def crcencode():
    bits="1"
    m="10101"
    r="0000"
    bits+=r
    div = bit_to_int(bits)

    divd = bit_to_int(m)

    rem=modulus_2_division(bits,m)
    reminder=bit_to_int(rem)
    msg=bit_to_int(bits)
    return np.binary_repr(msg+reminder+1)


def crcdecode(msg):
    if int(modulus_2_division(msg,"10101"))==0:
        print("NO ERROR\nMessage is",msg)
    else:
        print("ERROR DETECTED")
    


 
crcdecode(crcencode())