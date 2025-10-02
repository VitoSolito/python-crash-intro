str="012345678"
str_empty=""
for i in range(0,len(str)):
    if i%2==0 : str_empty = str_empty + str[i] + ", "
print("Expected output: ", str_empty)