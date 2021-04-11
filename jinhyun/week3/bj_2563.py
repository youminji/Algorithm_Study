import sys

N = int(sys.stdin.readline())
paper = [[0 for i in range (100)] for j in range(100)]
temp = [1,1,1,1,1,1,1,1,1,1]
answer = 0

for n in range(N):
    square_paper = sys.stdin.readline().split()
    row_index = 90 - int(square_paper[1])
    column_index = int(square_paper[0])
    for c in range(row_index, row_index+10):
        paper[c][column_index:column_index+10] = temp


for arr in paper:
    answer = answer + sum(arr)
print(answer)