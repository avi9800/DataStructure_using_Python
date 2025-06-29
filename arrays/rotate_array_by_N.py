array = [1,2,3,4,5,6,7]


def reverse(start,end,arr):
    arr = arr.copy()
    while(start < end):
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr

# Rotation is taken as left

def brute_force(arr,N):
    arr = arr.copy()

    if N >= len(arr):
        N = N%len(arr)
    
    if len(arr)<=1 or N <= 0:
        return arr

    for i in range(N): #Defining number of overall rotation to make in terms of ony place
        temp = arr[0]
        for j in range(1,len(arr)): #Rotating the array by one place
            arr[j-1] = arr[j]
        
        arr[len(arr)-1] = temp
    
    print("Using Brute force method ",arr)

N = int(input("Please enter number of rotations: "))

def better(arr, N):
    arr = arr.copy()

    if N >= len(arr):
        N = N%len(arr)
    
    if len(arr)<=1 or N <= 0:
        return arr
    
    temp = arr[:N] #Storing left halve of array

    for i in range(N,len(arr)):     #Shifting right halve of array to left
        arr[i],arr[i-N] = arr[i-N],arr[i]
    
    for j in range(len(arr)-N,len(arr)):  #Shifting left halve to the right
        arr[j] = temp[j-(len(arr)-N)]

    print("Using better method",arr)



def optimal(arr,N):
    arr = arr.copy()

    if N >= len(arr):
        N = N%len(arr)
    
    if len(arr)<=1 or N <= 0:
        return arr

    arr = reverse(0,N-1,arr)    #Reversing left halve of the array
    arr = reverse(N,len(arr)-1,arr)     #Reversing right halve of the array
    arr = reverse(0,len(arr)-1,arr)     #Reversing the whole array

    print("Using optimal method",arr)

    

brute_force(array,N)
better(array,N)
optimal(array,N)
