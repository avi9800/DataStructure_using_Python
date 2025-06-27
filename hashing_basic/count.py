from collections import OrderedDict
def count(arr):
    res = OrderedDict()
    for i in arr:
        if i in res.keys():
            res[i]+=1
        else:
            res[i]=1

    print(res)

arr = [7,2,3,4,5,1,4,4,1,2,4,5]
count(arr)