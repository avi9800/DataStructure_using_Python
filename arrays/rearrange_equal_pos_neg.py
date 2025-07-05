def bruteforce(arr):
    pos = []
    neg = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)

    p = 0
    n = 0
    for i in range(len(arr)):
        if i%2 == 0:
            arr[i] = pos[p]
            p+=1
        else:
            arr[i] = neg[n]
            n+=1


    print(arr)


def optimal(arr):
    pos = 0
    neg = 1
    if len(arr) <= 2:
        return arr
    
    result = [0] * len(arr)
    for i in range(len(arr)):
        if arr[i] < 0:  #negative
           result[neg] = arr[i]
           neg+=2
        else:   #positive
            result[pos] = arr[i] 
            pos+=2
    
    print(result)

arr = [-1,2,4,5,-2,-6]
optimal(arr)
