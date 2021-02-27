import sys
import collections

while True:
    input = sys.stdin.readline()
    if input == ".\n":
        break
    else:
        l = len(input)
        stack = collections.deque()
        flag = True
        for idx in range(l):
            if input[idx] == "(":
                stack.append("(")
            elif input[idx] == ")":
                if len(stack) == 0:
                    flag = False
                    break
                else:
                    temp = stack.pop()
                    if temp != "(":
                        flag= False
                        break
            elif input[idx] == "[":
                stack.append("[")
            elif input[idx] == "]":
                if len(stack) == 0:
                    flag = False
                    break
                else:
                    temp = stack.pop()
                    if temp != "[":
                        flag = False
                        break

        if len(stack) != 0:
            flag = False
        if flag:
            print("yes")
        else:
            print("no")
        flag = True