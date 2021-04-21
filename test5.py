def Rearrange(arr,n):
    i=0
    j=n-1
    while(True):
        while(arr[i]<0 and i<n):
            i+=1
        while(arr[j]>0 and j>=1):
            j-=1
        if (i<j):
            arr[i],arr[j]= arr[j],arr[i]
        else:
            break

arr=[-5,6,-9,8,-7,2,1]
n=len(arr)
Rearrange(arr,n)
print(*arr)
