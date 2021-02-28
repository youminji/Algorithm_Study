import sys
input = sys.stdin.readline().split()
array = [i for i in range(1, int(input[0])+1)]
l = len(array)
incre = int(input[1]) - 1
idx = incre
answer = []
while True:
    if len(array) == 0:
        break
    if idx >= len(array):
        idx = idx%len(array)
    answer.append(array[idx])
    del array[idx]
    idx = idx + incre

ans = "<"
for v in answer:
    ans = ans + str(v) + ", "
ans = ans[:-2]
ans = ans + ">"
print(ans)