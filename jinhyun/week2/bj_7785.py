import sys
N = int(sys.stdin.readline())
answer = {}
for i in range(N):
    input = sys.stdin.readline().split()
    if input[1] == "enter":
        answer[input[0]] = "enter"
    else:
        if input[0] in answer:
            del answer[input[0]]

answer = sorted(answer, reverse=True)
for name in answer:
    print(name)