def insertion_sort(l):
    for i in range(1, len(l)):
        j = i
        while l[j-1] > l[j] and j>0:
            l[j-1], l[j] = l[j], l[j-1]
            j -=1
    return l        
        
print(insertion_sort([2,1,6,2]))  