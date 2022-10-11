def Heapify(arr, n,  i):
    largest  = i
    left = 2*i +1
    right = 2*i+2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right 
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Heapify(arr, n, largest)

arr = [3,6,8,1,2,6,8,3]
n = len(arr)
def heapsort(arr):
    # Swap 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)
    return arr
    
    
# create Max  heapify
for i in range(n//2-1, -1, -1):
    Heapify(arr, n, i)

print(heapsort(arr))  