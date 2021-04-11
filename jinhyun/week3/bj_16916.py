import sys

S = sys.stdin.readline().split()[0]
P = sys.stdin.readline().split()[0]

len_P = len(P)
len_S = len(S)
hasing_P = 0
hasing_S_sub = 0
flag = False


for i in range(len_P):
    hasing_P = (hasing_P + ord(P[i])*(2**(len_P-i-1)))%1000000
    hasing_S_sub = (hasing_S_sub + ord(S[i])*(2**(len_P-i-1)))%1000000

if hasing_P != hasing_S_sub:
    for j in range(1, len_S - len_P):
        hasing_S_sub = ((hasing_S_sub - ord(S[j-1])*(2**(len_P-1)))*2 + ord(S[j+len_P-1]))%1000000
        if hasing_S_sub == hasing_P:
            flag = True
            break
else:
    flag = True

if flag:
    print(1)
else:
    print(0)
