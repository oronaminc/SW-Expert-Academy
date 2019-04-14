T = [5,-2,3,8,6]
def solution(T):
    n=len(T)
    for i in range(1,n):
        t1 = T[:i]
        t2 = T[i:]
        print(t1, max(t1))
        print(t2, min(t2))
        print()
        if max(t1) < min(t2):
            return i
print(T)
print(solution(T))