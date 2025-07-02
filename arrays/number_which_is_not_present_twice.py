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

def better(arr):
    maximum = max(arr)
    missing = [0] * maximum
    for i in arr:
        missing[i-1] +=1
    print(missing)
    for x in range(len(missing)):
        if missing[x] == 1:
            print(x + 1)

#Using XOR Method
def optimal(arr):
  missing = 0
  for i in arr:
    missing ^= i
  
  print(missing)

arr = [1, 1, 2, 2, 7, 7, 4, 4, 5, 5,-5]
optimal(arr)

