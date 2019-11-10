import numpy as np
from bitarray import bitarray


def xor(a, b): 
  
    # initialize result 
    result = [] 
  
    # Traverse all bits, if bits are 
    # same, then XOR is 0, else 1 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
  
    return ''.join(result)


def mod2div(divident, divisor): 
  
    # Number of bits to be XORed at a time. 
    pick = len(divisor) 
  
    # Slicing the divident to appropriate 
    # length for particular step 
    tmp = divident[0 : pick] 
  
    while pick < len(divident): 
  
        if tmp[0] == '1': 
  
            # replace the divident by the result 
            # of XOR and pull 1 bit down 
            tmp = xor(divisor, tmp) + divident[pick] 
  
        else:   # If leftmost bit is '0' 
            # If the leftmost bit of the dividend (or the 
            # part used in each step) is 0, the step cannot 
            # use the regular divisor; we need to use an 
            # all-0s divisor. 
            tmp = xor('0'*pick, tmp) + divident[pick] 
  
        # increment pick to move further 
        pick += 1
  
    # For the last n bits, we have to carry it out 
    # normally as increased value of pick will cause 
    # Index Out of Bounds. 
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


def crcincode():
    bits="1"
    m="10101"
    r="0000"
    bits+=r
    div=int(0)
    divd=int(0)
    for i in bits:
        div=2*div+int(i)
        
    for i in m:
        divd=2*divd+int(i)


    rem=mod2div(bits,m)
    reminder=bit_to_int(rem)
    msg=bit_to_int(bits)
    return np.binary_repr(msg+reminder+1)


def crcdecode(msg):
    if int(mod2div(msg,"10101"))==0:
        print("NO ERROR\nMessage is",msg)
    else:
        print("ERROR DETECTED")
    


 
crcdecode(crcincode())