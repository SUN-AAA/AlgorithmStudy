#prices 큐 -> price = pop(0) -> cnt += 1 -> if 비교대상 < price, break
#pop 할 때마다 cnt값을 계산해 answer 배열에 저장

#pop(0)을 사용하면 시간 초과 발생
#popleft을 이용해 시간 단축

#pop과 popleft의 차이
#pop(0)은 리스트에서 0번 인덱스 원소를 제거한 후 나머지 원소들을 한 칸씩 앞으로 당겨야함(shift) = 리스트를 억지로 큐처럼 사용하는 방식 -> 시간 복잡도 O(n)
#popleft은 head의 위치를 이동 = 큐 -> 시간복잡도 O(1)

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        cnt = 0
        price = prices.popleft()
        for i in prices:
            cnt += 1
            if i < price:
                break
        answer.append(cnt)
    return answer

print(solution([1, 2, 3, 2, 3]))
print(solution([100,10,200,300,350,17]))
print(solution([2,1]))
print(solution([5,4,3,2,1]))
print(solution([5,4,5,5]))
print(solution([3,1,2]))