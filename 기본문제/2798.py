#n장의 카드 중 3장의 카드를 순서대로 뽑는 경우의 수 = n * (n-1) * (n-2)
#3중 for문으로 세 카드 값을 합산 (이때 자기 자신이 중복되지 않도록 해야됨) -> 최적의 수면 best 변수에 저장

#피드백: for문에서 range값을 건들어 주면 if i == j나 if k==i of k == j 조건을 안쓰고도 풀 수 있음
"""
temp = input().split()
n = int(temp[0])
m = int(temp[1])

card = input().split()
cards = []
for num in card:
    cards.append(int(num))

best = 0
for i in range(0,n):
    for j in range(0,n):
        if i == j:
            continue
        
        for k in range(0,n):
            if k == i or k == j:
                continue

            tot = cards[i] + cards[j] + cards[k]

            if tot <= m and tot > best:
                best = tot


print(best)
"""

#피드백 반영
#순열 -> 조합

temp = input().split()
n = int(temp[0])
m = int(temp[1])

card = input().split()
cards = []
for num in card:
    cards.append(int(num))

best = 0
for i in range(0,n-2):
    for j in range(i,n-1):
        for k in range(j,n):
            tot = cards[i] + cards[j] + cards[k]

            if tot <= m and tot > best:
                best = tot


print(best)