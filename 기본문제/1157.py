s = input().upper()
alpha = []
count = []

for c in s:
    if c not in alpha:
        alpha.append(c)
        count.append(s.count(c))

max = count[0]
idx = 0
for i in range(0,len(count)):
    if count[i] > max:
        max = count[i]
        idx = i

if count.count(max) != 1:
    print("?")
else:
    print(alpha[idx])
