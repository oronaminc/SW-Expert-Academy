from collections import Counter
T = int(input())
for _ in range(T):
    N = int(input())
    LIST = list(map(int,input().split()))
    print("#{} {}".format(_+1,Counter(LIST).most_common(1)[0][0]))