#행별로 입력받은 후 2차원 배열로 만듦
#max 값 찾음 & max 값의 행, 열 인덱스 저장
#행은 인덱스 + 1
#열은 인덱스 + 1
#출력

nums = []
for i in range(0,9):
    lst = input().split()
    nums.append(lst)

max = int(nums[0][0])
row = 0
col = 0

for i in range(0,9):
    for j in range(0,9):
        if int(nums[i][j]) > max:
            max = int(nums[i][j])
            row = i
            col = j

print(int(max),end="\n")
print(int(row) + 1,int(col) + 1)