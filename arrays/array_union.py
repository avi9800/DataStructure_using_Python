def brute_force(arr1, arr2):
    arr1 = arr1.copy()
    arr2 = arr2.copy()
    union = set()
    for a in arr1:
        union.add(a)
    for b in arr2:
        union.add(b)
    
    print(list(union))

def optimal(arr1, arr2):
    arr1 = arr1.copy()
    arr2 = arr2.copy()

    i,j,k = 0,0,0
    result = []


    while (i< len(arr1) and j < len(arr2)):
        #Find smallest element between arr1 and arr2
        #If the element is not present before place then add it
        if arr1[i] <= arr2[j]: 
            if len(result) == 0:
                result.append(arr1[i])
                i+=1
                k+=1
            else:
                if arr1[i] != result[k-1]:
                    result.append(arr1[i])
                    i+=1
                    k+=1
                else:
                    i+=1        
        elif arr1[i] >= arr2[j]:
            if len(result) == 0:
                result.append(arr2[j])
                j+=1
                k+=1
            else:
                if arr2[j] != result[k-1]:
                    result.append(arr2[j])
                    j+=1
                    k+=1
                else:
                    j+=1   
    
    #Adding rest of the unique elements
    while(i != len(arr1) or j != len(arr2)):
        if i < len(arr1):
            if arr1[i] != result[k-1]:
                result.append(arr1[i])
                i+=1
                k+=1
        elif j < len(arr2):
            if arr2[j] != result[k-1]:
                result.append(arr2[j])
                j+=1
                k+=1
            else:
                j+=1

    print(result)


array1 = [1,2,3,3,4,6,7,7]
array2 = [2,3,5,5,5,5,8,8,9,9,10]

optimal(array1, array2)