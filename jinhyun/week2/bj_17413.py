word = input()
l = len(word)
temp = ""
answer = ""
flag = True
for i in range (l):
    if word[i] == " ":
        if flag:
            answer = answer + "".join(reversed(temp)) + " "
            temp = ""
        else:
            temp = temp + word[i]
    elif word[i] == "<":
        if temp != "":
            answer = answer + "".join(reversed(temp))
            temp = ""
        flag = False
        temp = temp + word[i]
    elif word[i] == ">":
        temp = temp + word[i]
        flag = True
        answer = answer + temp
        temp = ""
    else:
        temp = temp + word[i]
    if i == l-1:
        if temp != "":
            answer = answer
            answer = answer + "".join(reversed(temp))
        print(answer)