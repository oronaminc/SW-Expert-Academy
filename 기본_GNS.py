T = int(input())
for _ in range(T):
    A,B = input().split()
    LIST = list(input().split())
    NUM_STR = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    LIST_NUM = [NUM_STR.index(x) for x in LIST]
    LIST_SORT = sorted(LIST_NUM)
    LIST_SORT_STR = [NUM_STR[x] for x in LIST_SORT]
    print(A)
    print(' '.join(LIST_SORT_STR))