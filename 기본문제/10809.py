#단어 입력받음
#a 부터 z까지 반복문 돌림
#단어 첫글자부터 마지막 글자까지 반복문 돌리며 해당 알파벳이 단어에 들어있는지 확인
#들어있다면 인덱스 출력, 없다면 -1 출력

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