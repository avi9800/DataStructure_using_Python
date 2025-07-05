def bruteforce(arr):
    result = []
    for i in range(len(arr)-1):
        leader = True
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                leader = False
                break
        if leader:
            result.append(arr[i])
    print("Leaders = ",result)

def optimal(arr):
    leader = []
    maximum = -1
    #Check for maximum using DP
    for i in range(len(arr)-1,-1,-1):
        if arr[i] > maximum:
            maximum = arr[i]
            leader.append(arr[i])
    
    print(sorted(leader, reverse=True))

arr = [10,22,12,3,0,6]
optimal(arr)
