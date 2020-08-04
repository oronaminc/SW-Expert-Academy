for t in range(10):
    T, WORD, SENTENCE = int(input()), input(), input()
    print("#{} {}".format(T, len(SENTENCE.split(sep=WORD))-1))