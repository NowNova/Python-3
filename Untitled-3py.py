q = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}
r = {11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
w = {10: "десять", 20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят", 60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят", 90: "девяносто"}
e = {100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот", 600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот", 1000: "тысяча"}

str2 = ""
n = int(input())
n1 = n % 10
n2 = (n - n1) % 100
n3 = (n - n2 - n1) % 1000
n4 = n % 100

if n < 10:
    print(q.get(n))
elif 10 < n < 20:
    print(r.get(n))
elif n >= 10 and  n in w:
    print(w.get(n))
elif 100 > n >= 20:
    print(f"{w.get(n2)} {q.get(n1)}")
elif n >= 100 and  n in e:
    print(e.get(n))
elif n >= 100 and n4 in r:
    print(f"{e.get(n3)} {r.get(n4)}")
elif n >= 100 and n2 in w and n1 == 0:
    print(f"{e.get(n3)} {w.get(n2)}")
elif n >= 100 and n2 ==0  and n1 == 0 and n3 == 0:
    print(f"{e.get(n)}")
elif n >= 100:
    print(f"{e.get(n3)} {w.get(n2)} {q.get(n1)}")