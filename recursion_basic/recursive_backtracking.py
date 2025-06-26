def forward(i):
    if i <= 0:
        return
    else:
        forward(i-1)
        print(i)

def backward(i, N):
    if i > N:
        return
    backward(i+1,N)
    print(i)

backward(1,10)


