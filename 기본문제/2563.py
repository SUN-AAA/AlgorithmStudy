#도화지는 100 * 100 픽셀, 모두 0으로 초기화
#여기서 색종이 좌표에 해당하는 부분의 값을 -1로 변경
#-1의 개수가 넓이가 됨

paper = [[0] * 100 for i in range(100)]
n = int(input())
p = []

for i in range(0,n):
    temp = input().split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    p.append(temp)

for i in range(0,n):
    for j in range(0,10):
        for k in range(0,10):
            paper[p[i][0] + j][p[i][1] + k] = -1

area = 0
for i in range(0,100):
    for j in range(0,100):
        if paper[i][j] == -1:
            area += 1
print(area)