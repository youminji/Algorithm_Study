import sys

word = sys.stdin.readline().split()[0]
answer = 0
word_length = len(word)
idx = 0
while True:
    if idx == len(word):
        break
    if word[idx] == 'c' :
        try :
            if word[idx+1] in ('=', '-'):
                idx = idx+1
        except:
            pass
    elif word[idx] == 'd':
        try :
            if word[idx+1] == '-':
                idx = idx+1
            elif word[idx+1] == 'z':
                try :
                    if word[idx+2] == '=':
                        idx = idx+2
                except:
                    pass
        except:
            pass
    elif word[idx] == 'l':
        try :
            if word[idx+1] == 'j':
                idx = idx+1
        except:
            pass
    elif word[idx] == 'n':
        try:
            if word[idx+1] == 'j':
                idx = idx+1
        except:
            pass
    elif word[idx] == 's':
        try :
            if word[idx+1] == '=':
                idx = idx+1
        except:
            pass
    elif word[idx] == 'z':
        try :
            if word[idx+1] == '=':
                idx = idx+1
        except:
            pass
    answer = answer +1
    idx = idx +1

print(answer)