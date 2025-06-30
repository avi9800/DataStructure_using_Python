def bruteforce(arr):
    arr.sort()
    print("bruteforce - ",arr[len(arr)-2])


arr = [5,2,5,7,1,2,3,0,9]
bruteforce(arr)

def better(arr):
    fir = arr[0]
    for i in range(1,len(arr)):
        if fir < arr[i]:
            fir = arr[i]
    

    sec = -1
    for i in range(len(arr)):
        if sec < arr[i] and arr[i] < fir:
            sec = arr[i]
    
    print("better - ",sec)

arr = [5,2,5,7,1,2,3,0,9]
better(arr)

def optimal(array):
    temp = [-1]*2

    for i in range(len(array)):
        if temp[1] < array[i]:
            temp[0] = temp[1]
            temp[1] = array[i]

    
    print("optimal - ",temp[0])

arr2 = [5,2,5,7,1,2,3,0,9]
optimal(arr2)