for _ in range(10):
    N = int(input())
    STRING = input()
    LIST, LEFT, RIGHT, FLAG = [0]*4, ['(', '[', '{', '<'], [')', ']', '}', '>'], True
    for item in STRING:
        if item in LEFT: LIST[LEFT.index(item)] += 1
        if item in RIGHT: LIST[RIGHT.index(item)] -= 1
        if -1 in LIST:
            FLAG = False
            break
    if FLAG and LIST.count(0) != 4: FLAG = False
    print("#{} {}".format(_+1, int(FLAG)))