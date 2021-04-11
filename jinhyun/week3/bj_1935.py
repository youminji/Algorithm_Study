import sys
import collections

N = int(sys.stdin.readline())
circul = sys.stdin.readline().split()[0]
name = {}
stack = collections.deque()

for t in range (N):
    name[chr(ord('A')+ t)] = int(sys.stdin.readline())

for word in circul:
    if word in ('+', '-', '*', '/'):
        temp2 = stack.pop()
        temp1 = stack.pop()
        if word == '+':
            stack.append(temp1+temp2)
        elif word == '-':
            stack.append(temp1-temp2)
        elif word == '*':
            stack.append(temp1*temp2)
        elif word == '/':
            stack.append(temp1/temp2)
    else:
        stack.append(name[word])

print(format(stack.pop(), ".2f"))