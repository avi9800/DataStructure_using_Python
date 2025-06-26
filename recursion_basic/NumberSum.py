def sum_of_num(N):
    if N == 0:
        return 0
    else:
        return N+sum_of_num(N-1)

print(sum_of_num(3))