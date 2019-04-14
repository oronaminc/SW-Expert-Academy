from sys import stdin

input = stdin.readline
flag=True
check=0
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [input().strip() for i in range(n)]
    for i in arr:
        for j in arr:
            if i in j:
                check += 1
        if check > 1:
            flag = False
        check = 0
    if flag:print("YES")
    else:print("NO")
    flag=True


"""

def check(pset, num):
    for i in range(1, len(num)):
        if num[:i] in pset:
            print("미치겠다",num[:i])
            return True
    return False
    
def solution(n):    
    pset = set()
    for _ in range(n):
        pnum = f.readline().strip()
        pset.add(pnum)
    print("pset :",pset)
    for pnum in pset:
        if check(pset, pnum):
            print("NO")
            return
    print("YES")

f = open(0)
c = int(f.readline())
for _ in range(c):
    n = int(f.readline())
    solution(n)
f.close()
"""