#같은 x좌표 2개, 같은 좌표 2개가 있어야 조건에 맞는 직사각형을 만들 수 있음.
#세 점을 입력 받을 때 x좌표 따로 y좌표 따로 리스트로 저장
#각 리스트에서 하나밖에 없는 값을 네 번째 점의 좌표로 설정

x = []
y = []
p_x = 0
p_y = 0

for i in range(0,3):
    p = input().split()
    x.append(p[0])
    y.append(p[1])

for p in x:
    if x.count(p) == 1:
        p_x = int(p)

for p in y:
    if y.count(p) == 1:
        p_y = int(p)

print(p_x,p_y)