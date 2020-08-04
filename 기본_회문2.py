def is_palindrome(WORD):
    pal_len = word_len//2 if word_len%2==0 else word_len//2+1
    for word_idx in range(pal_len):
        if WORD[word_idx] != WORD[len(WORD)-word_idx-1]: return False
    return True

for _ in range(10):
    N = int(input())
    LIST = [[x for x in input()] for i in range(100)]
    LIST_reverse = list(map(list, zip(*LIST)))
    FLAG = False
    for word_len in range(100, 0, -1):
        for col_idx in range(100):
            for idx in range(100-word_len+1):
                if is_palindrome(LIST[col_idx][idx:idx+word_len]) or is_palindrome(LIST_reverse[col_idx][idx:idx+word_len]):
                    FLAG = True
                    break
        if FLAG: break
    print("#{} {}".format(_+1, word_len))