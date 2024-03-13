str = input("")
str += " "
n = 0
str2 = ""

for i in range(1, len(str)):
    if str[i] == str[i - 1]:
        n += 1
    elif n != 0:
        n += 1
        str2 += "%s%d" %(str[i - 1], n) 
        n = 0
    else:
        str2 += "%s" %(str[i - 1]) 
        n = 0
# YYYYggkeeeAAABV
print(str)
print(str2)
