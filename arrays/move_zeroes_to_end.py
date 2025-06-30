array = [0,1,0,2,4,0,0,0,4,0,8]

def bruteforce(arr):
    arr = arr.copy()
    zeros = []
    non_zeros = []

    #Storing all zeroes and non zeroes in two arrays separately
    for i in arr:
        if i == 0:
            zeros.append(0)
        else:
            non_zeros.append(i)
    
    #Merging the final array
    for i in range(len(arr)):
        if i<len(non_zeros):
            arr[i] = non_zeros[i]
        else:
            arr[i] = zeros[i-len(non_zeros)]
    
    print("Resultant array = ", arr)



def optimal(arr):
    arr = arr.copy()
    j = 0
    for i in range(len(arr)):
        if i != j and arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
        if arr[j] != 0:
            j+=1
        
    print("Resultant array = ", arr)


bruteforce(array)
optimal(array)