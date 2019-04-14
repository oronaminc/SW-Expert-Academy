from sys import stdin

t=''
for i in stdin.read().split():
    if i == "<br>":
        print(t)
        t=""
    elif i == "<hr>":
        if i:
            print(t)
            t=""
        print('-'*80)
    else:
        I = t + ' ' + i if t else i
        if len(I)>80:
            print(t)
            t = i
        else: t = I
if t:print(t)