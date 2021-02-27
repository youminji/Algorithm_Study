import sys
import collections

middle = sys.stdin.readline()
answer = ""

v = collections.deque()
circul = collections.deque()
l = len(middle)
for idx in range(l):
    if middle[idx] in ('+','-','*','/','(',')'):
        if middle[idx] == '+':
            if len(circul) == 0:
                circul.append(middle[idx])
        elif middle[idx] == '-':
            if len(circul) == 0:
                circul.append(middle[idx])
        elif middle[idx] == '*':
            circul.append(middle[idx])
        elif middle[idx] == '/':
            circul.append(middle[idx])
        elif middle[idx] == '(':
            pass
        elif middle[idx] == ')':
            pass
    else:
        v.append(middle[idx])
