#배열 순회 -> 현재 값보다 큰 값이 배열 안에 있다면 pop 하고 append, 없다면 pop & answer += 1
#이때 location 값을 감소.
#len(priorities) == 1일 때 for문이 실행되지 않아 종료가 while문이 종료되지 않는 문제가 발생함 -> 따로 조건으로 빼서 바로 answer + 1 반환하도록 처리

def solution(priorities, location):
    answer = 0
    while True:
        if len(priorities) == 1:
            return answer + 1
        for j in range(1,len(priorities)):
            if priorities[0] < priorities[j]:
                temp = priorities.pop(0)
                priorities.append(temp)
                location = (location - 1) % len(priorities)
                break
            elif j == len(priorities)-1 and priorities[0] >= priorities[j]:
                answer += 1
                if 0 == location:
                    return answer
                
                location = (location - 1) % len(priorities)
                priorities.pop(0)
                

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))
print(solution([5],0))