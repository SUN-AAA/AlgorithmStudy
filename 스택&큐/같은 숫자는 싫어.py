#반복문으로 배열 값 순회 -> 배열의 다음 값과 값이 다르면 append + 맨 마지막 값은 그냥 append

def solution(arr):
    answer = []
    for i in range(0,len(arr) - 1):
        if arr[i] != arr[i + 1]:
            answer.append(arr[i])
    answer.append(arr[-1])
    
    return answer

arr1 = [1,1,3,3,0,1,1]
ans1 = solution(arr1)
print(ans1)


