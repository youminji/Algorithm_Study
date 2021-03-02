import sys

first_word = sys.stdin.readline().split()[0]
second_word = sys.stdin.readline().split()[0]

row = len(first_word)
column = len(second_word)
LCS = [[0 for j in range(column+1)] for i in range(row+1)]

for r in range(1, row+1):
    for c in range(1, column+1):
        if first_word[r-1] == second_word[c-1]:
            LCS[r][c] = LCS[r-1][c-1] + 1
        else:
            LCS[r][c] = max(LCS[r-1][c], LCS[r][c-1])

print(max(map(max, LCS)))

