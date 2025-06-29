array = [1,2,4,4,5,8]
def brute_force(arr):
    temp = arr.copy()
    temp.sort()
    j = 0
    for i in range(len(arr)):
        if arr[i] != temp[i]:
            j+=1

    if j == 0:
        print("sorted array")
    else:
        print("Not sorted array") 

brute_force(array)

def optimal(arr):
    j = True
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            j = False
            break
    
    if j:
        print("Sorted array ",arr)
    else:
        print("Not sorted array ",arr)

optimal(array)