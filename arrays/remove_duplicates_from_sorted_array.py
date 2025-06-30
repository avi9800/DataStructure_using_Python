array = [1,2,2,3,3,3,4,5,5,5,6]
def brute_force(arr):
    unique = set()
    for element in arr:
        unique.add(element)
    
    print(list(unique))
    print("Number of unique elements ",len(unique))


def optimal(arr):
    unique = 1
    temp = []
    temp.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            unique+=1
            temp.append(arr[i])

    print(temp)
    print("Number of unique elements ",unique)

if len(array) >= 1:
    brute_force(array)
    optimal(array)