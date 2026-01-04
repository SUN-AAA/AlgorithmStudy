#피드백: while문을 이용하면 깨끗한 코드를 짤 수 있음. 지금은 너무 더티코드ㅎㅋ

"""
n = int(input())
cnt = 0
for i in range(1,n):
    sum = i + (i // 1000000) + (i % 1000000 // 100000) + (i % 1000000 % 100000 // 10000) + (i % 1000000 % 100000 % 10000 // 1000) + (i % 1000000 % 100000 % 10000 % 1000 // 100) + (i % 1000000 % 100000 % 10000 % 1000 % 100 // 10) + (i % 1000000 % 100000 % 10000 % 1000 % 100 % 10)
    if sum == n:
        print(i)
        cnt += 1
        break

if cnt == 0:
    print(0)
"""

#피드백 반영
#while문을 이용해 i % 10을 구하고 i = i // 10으로 초기화하는 작업을 i == 0이 될때까지 반복하면 가능

n = int(input())
cnt = 0

for i in range(1,n):
    temp = i
    sum = i
    while i != 0:
        sum += i % 10
        i = i // 10
    
    if sum == n:
        cnt += 1
        print(temp)
        break

if cnt == 0:
    print(0)