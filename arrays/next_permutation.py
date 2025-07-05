def optimal(arr):
    #Find break point
    b = -1
    for i in range(len(arr)-1,0,-1):
        if arr[i-1] < arr[i]:
            b = i
            break
    #Find just greater number than arr[b-1]
    if b>= 0:
        for j in range(len(arr)-1,b-1,-1):
            if arr[j]>arr[b-1]:
                just_large = j
                break
        #swap the b-1 and just_large
        arr[b-1], arr[just_large] = arr[just_large], arr[b-1]

        #sort the rest of the array in ascending order
        arr[b:len(arr)] = sorted(arr[b:len(arr)])
    else:
        arr.reverse()
    print(arr) 
arr = [1,2,3,4,5]
optimal(arr)


