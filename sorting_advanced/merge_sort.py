#Function to merge
def merge(arr,low,high,mid,merge_type):
    l1 = low
    r1 = mid
    l2 = mid+1
    r2 = high
    temp = []

    while(l1<=r1 and l2<=r2):
        #Ascending Order
        if merge_type == "Ascending":
            if arr[l1] > arr[l2]:
                temp.append(arr[l2])
                l2+=1
            else:
                temp.append(arr[l1])
                l1+=1
        #Descending Order
        elif merge_type == "Descending":
            if arr[l1] < arr[l2]:
                temp.append(arr[l2])
                l2+=1
            else:
                temp.append(arr[l1])
                l1+=1
    
    if l1<=r1:
        temp.extend(arr[l1:(r1+1)])
    elif l2<=r2:
        temp.extend(arr[l2:(r2+1)])
    
    for x in range(low,high+1):
        arr[x] = temp[x-low]






#Function to divide 
def merge_sort(arr,low,high,merge_type):
    
    if low >= high:
        return

    mid = (low+high)//2

    merge_sort(arr,low,mid,merge_type)
    merge_sort(arr,mid+1,high,merge_type)
    merge(arr,low,high,mid,merge_type)
    return arr

array = [5,-4,3,-2,1]
array2 = [1,-2,3,-4,5]
print(merge_sort(array, 0,len(array)-1,'Ascending'))
print(merge_sort(array, 0,len(array2)-1,'Descending'))