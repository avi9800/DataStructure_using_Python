arr1 = [-1,2,-3,4,5]
temp1 = [-1,2,-3,4,5]

def insertion_descending(arr):
    for i in range(1,len(arr)):
        counter = i
        while(counter > 0):
            if arr[counter] > arr[counter-1]:
                arr[counter], arr[counter-1] = arr[counter-1], arr[counter]

            counter = counter - 1 
        

    return arr

arr2 = [5,4,3,2,1]
temp2 = [5,4,3,2,1]

def insertion_ascending(arr):
    for i in range(1,len(arr)):
        counter = i
        while(counter > 0):
            if arr[counter] < arr[counter-1]:
                arr[counter], arr[counter-1] = arr[counter-1], arr[counter]

            counter = counter - 1 
        

    return arr


print(temp1, "after sorting in descending order = ",insertion_descending(arr1))
print(temp2, "after sorting in ascending order = ",insertion_ascending(arr2))