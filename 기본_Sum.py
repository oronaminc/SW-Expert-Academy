for _ in range(10):
    MAX = float('-inf')
    T = int(input())
    LIST = [list(map(int,input().split())) for i in range(100)]
    LIST_reverse = list(map(list, zip(*LIST)))
    cross_sum1, cross_sum2 = 0, 0
    for idx in range(100):
        if MAX < sum(LIST[idx]): MAX = sum(LIST[idx])
        if MAX < sum(LIST_reverse[idx]): MAX = sum(LIST_reverse[idx])
        cross_sum1 += LIST[idx][idx]
        cross_sum2 += LIST[idx][99-idx]
    MAX = max(MAX, cross_sum1, cross_sum2)
    print("#{} {}".format(_+1, MAX))