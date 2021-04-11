import sys

N = int(sys.stdin.readline())
answer = 0

for i in range (N):
    save_alphabet = {}
    word = sys.stdin.readline().split()[0]
    flag = True
    compare_word = word[0]
    for alphabet in word:
        if compare_word != alphabet:
            if compare_word in save_alphabet:
                flag = False
                break
            else:
                save_alphabet[compare_word] = True
                compare_word = alphabet
    if compare_word in save_alphabet:
        flag = False
    if flag:
        answer = answer + 1

print(answer)