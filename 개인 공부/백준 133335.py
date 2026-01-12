#최대 대수, 최대 무게 주어짐
#다리 길이 크기의 큐를 만듦 -> 한 대 추가될 때마다 pop(0), append(truck_weights.pop(0))
#이때 만약 전체 무게 > 최대 무게 이라면 pop(0), append(0) (다리 위 최대 트럭 수는 current 배열 크기가 설정되어있어 초과될 일이 없음)
#pop 될때마다 answer(시간) += 1

def solution(bridge_length, weight, truck_weights):
    answer = 0
    current = [0] * bridge_length
    w = 0
    while truck_weights or w > 0:
        if truck_weights:
            
            end_p = current.pop(0)
            w -= end_p
            w += truck_weights[0]

            if w <= weight:
                temp = truck_weights.pop(0)
                current.append(temp)
                answer += 1
            else:
                w -= truck_weights[0]
                current.append(0)
                answer += 1

        else:
            answer += bridge_length
            break
    return answer

nwl = input().split()
n = int(nwl[0])
w = int(nwl[1])
l = int(nwl[2])

temp = input().split()
a = []
for i in range(0,n):
    a.append(int(temp[i]))

print(solution(w,l,a))