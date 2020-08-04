def is_palindrome(WORD):
    for word_idx in range(word_len):
        if WORD[word_idx] != WORD[N-word_idx-1]: return False
    return True

for _ in range(10):
    N = int(input())
    LIST = [[x for x in input()] for i in range(8)]
    LIST_reverse = list(map(list, zip(*LIST)))
    SUM, word_len = 0, N//2 if N%2==0 else N//2+1
    for col_idx in range(8):
        for idx in range(8-N+1):
            if is_palindrome(LIST[col_idx][idx:idx+N]): SUM += 1
        for idx in range(8-N+1):
            if is_palindrome(LIST_reverse[col_idx][idx:idx+N]): SUM += 1
    print("#{} {}".format(_+1, SUM))