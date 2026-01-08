#남은 작업 일수 계산 -> 배열로 저장
#배포 개수 계산 -> 배열로 저장
#배포 계수 계산 로직 : 배포 일자의 기준이 되는 날의 값(front 값)보다 남은 작업 일수 값(work[i] 값)이 작거나 같다면 같은 배포 날짜로 취급
#cnt로 날짜 수 세서 answer 배열에 저장

def solution(progresses, speeds):
    answer = []
    work = []

    for i in range(0,len(progresses)):
        days = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            days += 1
        work.append(days)

    work.append(101)                #마지막 묶음 계산을 위해 추가함...
    cnt = 0
    front = 0
    for i in range(0,len(work)):
        if i == 0:
            front = work[i]
            cnt = 1
        elif work[i] <= front:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            front = work[i]
    
    print(work, answer)
    return answer

#테스트
pro1 = [93,30,55]
sp1 = [1,30,5]
print(solution(pro1,sp1))

pro2 = [95, 90, 99, 99, 80, 99]
sp2 = [1, 1, 1, 1, 1, 1]
print(solution(pro2,sp2))