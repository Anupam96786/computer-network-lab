import pandas as pd

s = input("Enter a string:- ")

arr = list()

for i in s:
    binary_val = bin(ord(i))[2:]
    single_char_arr = [0] * (8-len(binary_val)) + list(map(int, list(binary_val)))
    single_char_arr.append(single_char_arr.count(1) % 2)
    arr.append(single_char_arr)

index = list(s)
columns = ['bit0', 'bit1', 'bit2', 'bit3', 'bit4', 'bit5', 'bit6', 'bit7', 'parity']

arr = pd.DataFrame(arr, index=index, columns=columns)
arr.loc['parity',:] = [list(arr.loc[:,col]).count(1) % 2 for col in columns]
arr = arr.astype(int)
print(arr)