from sys import stdin

for i in stdin.readlines():
    print(i)
    s, b, n,st = 0,0,0,0
    st=i.count(' ')
    for j in i:
        if 'a'<=j<='z': s +=1
        elif 'A'<=j<='Z': b += 1
        elif ord('0')<=ord(j)<=ord('9'): n +=1
    print(s,b,n,st)