#문자열 입력 받은 후 대문자로 변경
#문자열 속 알파벳의 종류와 나온 횟수를 각각 리스트에 저장
#나온 횟수 리스트에서 max 값을 찾고 max 값의 인덱스를 저장
#저장해둔 인덱스에 해당하는 알파벳 출력
#출력할 때 max 값이 1개가 아니라면 ? 출력

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
