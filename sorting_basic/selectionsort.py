def selection_ascending_sort(arr):
    min_index = -1
    for i in range(len(arr)-1):
        #Getting minimum number and it's index of the list
        minimum = arr[i]
        for j in range(i+1,len(arr)):
            if minimum > arr[j]:
                minimum = arr[j]
                min_index = j
        
        
        #Swapping with first position
        t = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = t


    return arr
            


def selection_descending_sort(arr):
    max_index = -1
    for i in range(len(arr)-1):
        maximum = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j] > maximum:
                maximum = arr[j]
                max_index = j

        t = arr[i]
        arr[i] = arr[max_index]
        arr[max_index] = t
    
    return arr


arr1 = [1,2,3,4,5]
print(arr1)
print("after sorting = ",selection_descending_sort(arr1))

arr2 = [5,4,3,2,1]
print(arr2)
print("after sorting = ",selection_ascending_sort(arr2))


        