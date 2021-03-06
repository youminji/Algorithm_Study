import sys

N = int(sys.stdin.readline())

five_divide = N // 5
answer = -1
for i in range (five_divide+1):
    temp = N - 5*i
    if temp%3 == 0:
        t = i + temp//3
        if answer == -1:
            answer = t
        elif answer > t:
            answer = t

print(answer)