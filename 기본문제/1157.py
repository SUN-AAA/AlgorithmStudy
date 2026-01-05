#문자열 입력 받은 후 대문자로 변경
#문자열 속 알파벳의 종류와 나온 횟수를 각각 리스트에 저장
#나온 횟수 리스트에서 max 값을 찾고 max 값의 인덱스를 저장
#저장해둔 인덱스에 해당하는 알파벳 출력
#출력할 때 max 값이 1개가 아니라면 ? 출력

#피드백: count 함수는 파이썬 문법이므로 파이썬 함수를 쓰지 않고 푸는 연습을 해야함.
#피드백2: count 함수를 써서 오히려 더 복잡한 로직이 되었으니 좀 더 나은 로직을 고민해 봐야함.

"""
s = input().upper()
alpha = []
count = []

for c in s:
    if c not in alpha:
        alpha.append(c)
        count.append(s.count(c))

max = count[0]
idx = 0
for i in range(0,len(count)):
    if count[i] > max:
        max = count[i]
        idx = i

if count.count(max) != 1:
    print("?")
else:
    print(alpha[idx])
"""

#피드백 반영
#문자열 순회하며 {문자: 개수} 형식의 딕셔너리 생성 -> value값 순회하며 max값 찾음 
#(순회하면서 동시에 계산) max값이 중복되면 times(중복 상태를 저장하는 변수) 값을 1로 변경 -> times = 0 이면 문자 출력 else '?' 출력

s = input().upper()
s_dic = {}

for c in s:
    if c not in s_dic:
        s_dic[c] = 1
    else:
        s_dic[c] += 1

max = 0
key = ''
times = 0

for k,v in s_dic.items():
    if v > max:
        max = v
        key = k
        times = 0
    elif v == max:
        times = 1

if times == 0:
    print(key)
else:
    print('?')
