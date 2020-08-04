for _ in range(10):
    N = int(input())
    STR = input()
    SUM = 0
    for idx, item in enumerate(STR):
        if idx%2 == 0: SUM += int(item)
    print("#{} {}".format(_+1, SUM))