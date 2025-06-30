def brute_force(arr,N):
    arr = arr.copy()
    for i in range(1,N+1):
        temp = 0
        for j in arr:
            if i == j:
                temp+=1
        if temp == 0:
            print("Missing number is ",i)
            break

def better(arr,N):
    arr = arr.copy()
    result = {i: 0 for i in range(1,N+1)}
    for i in arr:
        #if i in result.keys():
            result[i]=1
    
    for j in result.keys():
        if result[j] == 0:
            print("Missing number is ",j)
            break


def optimal(arr,N):
    arr = arr.copy()
    s1 = (N*(N+1))/2
    s2 = 0
    for i in arr:
        s2+=i
    
    if s1 != s2:
        print("Missing number is ", int(s1-s2))



array = [1,2,3,5,6,7]
N = max(array)
optimal(array,N)