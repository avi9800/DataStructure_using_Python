arr1 = [-1,2,-3,4,5]
temp1 = [-1,2,-3,4,5]


def bubble_descending(arr):
    if len(arr) < 2:
        return arr

    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] < arr[j+1]:
                swap = True
                arr[j], arr[j+1] = arr[j+1],arr[j]
        
        if not swap:
            print("No swap")
            return arr
    
    return arr


arr2 = [5,4,3,2,1]
temp2 = [5,4,3,2,1]

def bubble_ascending(arr):
    if len(arr) < 2:
        return arr

    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                swap = True
                arr[j], arr[j+1] = arr[j+1],arr[j]
        
        if not swap:
            print("No swap")
            return arr
    
    return arr

print(temp1, "after sorting in descending order = ",bubble_descending(arr1))
print(temp2, "after sorting in ascending order = ",bubble_ascending(arr2))