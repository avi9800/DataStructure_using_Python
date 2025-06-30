def brute_force(arr1, arr2):
    arr1 = arr1.copy()
    arr2 = arr2.copy()
    result = set()

    for i in arr1:
        for j in arr2:
            if i == j:
                result.add(i)
    
    print(list(result))


def optimal(arr1, arr2):
    arr1 = arr1.copy()
    arr2 = arr2.copy()
    result = []

    i = 0
    j = 0
    k = 0

    while(i != len(arr1) and j != len(arr2)):
        if arr1[i] == arr2[j]:
            if len(result) == 0:
                result.append(arr1[i])
                i+=1
                j+=1
                k+=1
            else:
                if result[k-1] != arr1[i]:
                    result.append(arr1[i])
                    i+=1
                    j+=1
                    k+=1
        else:
            if arr1[i] > arr2[j]:
                j+=1
            else:
                i+=1
    
    print(result)




array1 = [1,2,3,3,4,10]
array2 = [1,2,3,4,5,5,5,8,8,9,9,10]

optimal(array1, array2)