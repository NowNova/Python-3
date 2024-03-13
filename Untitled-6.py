str = input("").split()
str2 = ""
for i in str:
    str2 += i[0]
for i in range(0, len(str2)):
    if "a" <= str2[i] <= "z":
        print(str2[i].upper(), end = "")
    if "а" <= str2[i] <= "я":
        print(chr(ord(str2[i]) - 32), end = "")
    if str2[i] == "ё":
        print(chr(ord(str2[i]) - 80), end = "")
    if "A" <= str2[i] <= "Z" or "А" <= str2[i] <= "Я":
        print(str2[i], end = "")
    if str2[i] == "Ё":
        print(str2[i], end = "")





