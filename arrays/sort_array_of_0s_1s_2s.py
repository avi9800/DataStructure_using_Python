def better(arr):
    a = [0] * 3
    for i in arr:
        a[i] += 1
    x=0
    for i in range(len(a)):
        for j in range(x,a[i]):
            counter = j
            arr[j] = i
        x = counter
    
    print(arr)


def optimal(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while(mid <= high):
        print(low,mid,high)
        print(arr)
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid],arr[low]
            mid +=1
            low +=1
        elif arr[mid] == 1:
            mid +=1
        elif arr[mid] == 2:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -=1

arr = [1,2,1,0,2]
optimal(arr) 
