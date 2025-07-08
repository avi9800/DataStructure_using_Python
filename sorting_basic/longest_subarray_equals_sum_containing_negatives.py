def brute_force(arr, k):
    if len(arr) == 1:
        if arr[0] == k:
            return arr
        else:
            return []
    
    result = []
    for i in range(len(arr)):
        c = 0
        for j in range(i,len(arr)):
            #print(result)
            if c < k:
                c+=arr[j]
            if c > k:
                c = 0
                break
            if c == k:
                c = 0
                if len(result) < len(arr[i:j+1]):
                    result = arr[i:j+1]
                    break
    
    print(result)

def better(arr,k):  #IS the optimal solution if the array contains negatives else not
    if len(arr) == 1:
        if arr[0] == k:
            return arr
        else:
            return []
    
    presums = {}
    sums = 0
    maxLen = 0
    for i in range(len(arr)):
        sums+=arr[i]
        if sums == k:
            maxLen = i+1
        if sums - k in presums.keys():
            length = i - presums[sums - k]
            maxLen = max(maxLen, length)
        if sums not in presums.keys():
            presums[sums] = i
        print(maxLen)
    print(presums)
    



arr = [1,2,-3,-3,1,1,1,4,2,3]
k = 3
better(arr, k)
