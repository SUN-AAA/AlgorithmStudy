twoInt = input()
a = int(twoInt.split(" ")[0])
b = int(twoInt.split(" ")[1])

res = []

while a != 0 or b != 0:
    res.append(a + b)
    twoInt = input()
    a = int(twoInt.split(" ")[0])
    b = int(twoInt.split(" ")[1])

for r in res:
    print(r,end="\n")