#단어 입력받음
#a 부터 z까지 반복문 돌림
#단어 첫글자부터 마지막 글자까지 반복문 돌리며 해당 알파벳이 단어에 들어있는지 확인
#들어있다면 인덱스 출력, 없다면 -1 출력

#피드백: aplha를 모두 순회하면 시간 복잡도가 O(26*n)이 나오지만 사실 O(n)으로도 끝낼 수 있는 문제이니 고민해 봐야함.

s = input()
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(0,len(alpha)):
    cnt = 0
    for j in range(0,len(s)):
        if alpha[i] == s[j]:
            cnt += 1
            print(j, end=" ")
            break
    if cnt == 0:
        print(-1,end=" ")