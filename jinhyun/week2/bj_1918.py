import sys
import collections

middle = sys.stdin.readline().split()[0]
answer = ""
circul = collections.deque()
l = len(middle)
for idx in range(l):
    if middle[idx] in ('+','-','*','/','(',')'):
        if middle[idx] == '+':
            if len(circul) == 0:
                circul.append(middle[idx])
            else:
                while True:
                    temp = circul.pop()
                    if temp != '(':
                        answer = answer + temp
                        if len(circul) == 0:
                            circul.append(middle[idx])
                            break
                    else:
                        circul.append(temp)
                        circul.append(middle[idx])
                        break
        elif middle[idx] == '-':
            if len(circul) == 0:
                circul.append(middle[idx])
            else:
                while True:
                    temp = circul.pop()
                    if temp != '(':
                        answer = answer + temp
                        if len(circul) == 0:
                            circul.append(middle[idx])
                            break
                    else:
                        circul.append(temp)
                        circul.append(middle[idx])
                        break
        elif middle[idx] == '*':
            if len(circul) == 0:
                circul.append(middle[idx])
            else:
                temp = circul.pop()
                if temp in ('/', '*'):
                    answer = answer + temp
                    circul.append(middle[idx])
                else:
                    circul.append(temp)
                    circul.append(middle[idx])        
        elif middle[idx] == '/':
            if len(circul) == 0:
                circul.append(middle[idx])
            else:
                temp = circul.pop()
                if temp in ('/', '*'):
                    answer = answer + temp
                    circul.append(middle[idx])
                else:
                    circul.append(temp)
                    circul.append(middle[idx])
        elif middle[idx] == '(':
            circul.append(middle[idx])
        elif middle[idx] == ')':
            while True:
                temp = circul.pop()
                if temp == '(':
                    break
                else:
                    answer = answer + temp
    else:
        answer = answer + middle[idx]

if len(circul) != 0:
    while True:
        if len(circul) == 0:
            break
        answer = answer + circul.pop()
print(answer)
