#단어 입력받음
#a 부터 z까지 반복문 돌림
#단어 첫글자부터 마지막 글자까지 반복문 돌리며 해당 알파벳이 단어에 들어있는지 확인
#들어있다면 인덱스 출력, 없다면 -1 출력

#피드백: aplha를 모두 순회하면 시간 복잡도가 O(26*n)이 나오지만 사실 O(n)으로도 끝낼 수 있는 문제이니 고민해 봐야함.

"""
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
"""

#피드백 반영
#크기가 26인 res 배열을 -1로 초기화 -> 문자열 s를 순회하며 res[각 알파벳에 해당되는 인덱스] = 문자열에서 해당 알파벳의 인덱스 값으로 변경
alpha = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}

s = input()
res = [-1] * 26
for i in range(0,len(s)):
    if res[alpha[s[i]]] == -1:
        res[alpha[s[i]]] = i

for i in res:
    print(i,end=" ")