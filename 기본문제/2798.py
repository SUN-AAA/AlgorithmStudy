#n장의 카드 중 3장의 카드를 순서대로 뽑는 경우의 수 = n * (n-1) * (n-2)
#3중 for문으로 세 카드 값을 합산 (이때 자기 자신이 중복되지 않도록 해야됨) -> 최적의 수면 best 변수에 저장

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