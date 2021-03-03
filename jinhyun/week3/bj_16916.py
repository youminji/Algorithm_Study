import sys

S = list(sys.stdin.readline().split()[0])
P = list(sys.stdin.readline().split()[0])
S_len = len(S)
P_len = len(P)
idx_P = 0
idx_S = 0
flag = False

while True:
    if idx_S >= S_len - P_len + 1:
        break
    if S[idx_S] == P[idx_P]:
        count = 1
        while True:
            if count == P_len :
                flag = True
                break
            else:
                if S[idx_S+count] == P[idx_P+count]:
                    count = count+1
                else:
                    idx_P = 0
                    idx_S = idx_S + count
                    print(idx_S)
                    break
    else :
        idx_S = idx_S + 1
    
    if flag:
        break

if flag:
    print(1)
else:
    print(0)