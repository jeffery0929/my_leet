def ArrayChallenge(arr):
    maxnum=arr.pop(arr.index(max(arr)))
  
    arr=sorted(arr)
    total=0
    
    for i in range(len(arr)):
        total+=arr[i]
        for j in range(len(arr)):
            if(i!=j):
                total+=arr[j]
                if(total==maxnum):
                    return True
    
        for k in range(len(arr)):
            if i!=k:
                total-=arr[k]
                if total==maxnum:
                    return True

        total=0
    return False

def maxDiff(a):
    l = len(a)
    arr = []
    for i in range(l-1):
        for j in range(i+1, l):
            if a[j] > a[i]:
                diff = a[j] - a[i]
                arr.append(diff)
    if arr:
        return max(arr)
    else:
        return -1

print(maxDiff([14,20,4,12,5,11]))




