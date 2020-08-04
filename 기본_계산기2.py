for _ in range(10):
    stack, prior_idx = [], -1
    input();num=input()
    for idx, item in enumerate(num):
        if idx == prior_idx:continue
        if idx%2==0: stack.append(int(num[idx]))
        elif idx%2==1 and item=='*':
            stack[-1] = int(stack[-1])*int(num[idx+1])
            prior_idx = idx+1
    print("#{} {}".format(_+1,sum(stack)))