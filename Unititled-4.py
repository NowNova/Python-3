q = {}
str = list(("".join(i for i in input(""))).split(" "))
# str  = ("".join(i for i in input(""))).split(" ")

for i in range(0, len(str)):
    if str[i] not in q:
        q.update({str[i] : 1})
    else:
        q[str[i]] += 1
print(str)
DictValues = list(q.values())
print(DictValues)