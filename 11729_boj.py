N = int(input())
num=2**N-1
print(num)
def hanoi(N, from_, to_, axis_):
    if N==1:
        print(f"{from_} {to_}")
        return
    hanoi(N-1, from_, axis_, to_ )
    print(f"{from_} {to_}")
    hanoi(N-1, axis_, to_, from_)

hanoi(N,1,3,2)