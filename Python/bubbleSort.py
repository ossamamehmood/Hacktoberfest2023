def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        print(i)
        for j in range(n-i-1):
            print(arr,j)
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    
    

arr=[3,6,0,5]
bubblesort(arr)
print(arr)