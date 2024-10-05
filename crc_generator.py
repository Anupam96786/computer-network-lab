data_bit = input("Enter data bit:- ")
key = input("Enter key:- ")
data_bit_temp = data_bit + '0' * (len(key) - 1)

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
 
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0 : pick]
 
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
 
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    checkword = tmp
    return checkword

crc = mod2div(data_bit_temp, key)
data_to_sent = data_bit + crc

print(f"CRC:- {crc}")
print(f"Data to be sent:- {data_to_sent}")
