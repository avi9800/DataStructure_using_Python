def optimal(arr,k): #If the array doesn't have negatives
    if len(arr) == 1:
        if arr[0] == k:
            return arr
        else:
            return []
    
    
    maxLen,left, sums = 0,0,0
    for i in range(len(arr)):
        if sums == k:
            maxLen = max(maxLen, i-left)
        while(sums > k):
            sums-=arr[left]
            left +=1
        
        sums += arr[i]
    
    print(maxLen)


arr = [1,2,1,1,1,0,0,4,2,3]
k = 3
optimal(arr, k)
