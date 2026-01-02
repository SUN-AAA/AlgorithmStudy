s = input()

pal = 1
for i in range(0,int(len(s)/2)):
    if s[i] != s[len(s) - i - 1]:
        pal = 0
        print(0)
        break

if pal == 1:
    print(1)
