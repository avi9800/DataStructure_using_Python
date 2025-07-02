def brute_force(arr):
  a = {}
  for i in arr:
    if i not in a.keys():
      a[i] = 0
  
  for i in arr:
    a[i]+=1

  for i in a.keys():
    if a[i] == 1:
      print(i, "appears once")



arr = [1,1,2,2,3,3,4,4,5]
brute_force(arr)
