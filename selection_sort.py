def selection_sort(l):
    for i in range(len(l)-1):
        min_index = i
        for j in range(i, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        temp = l[i]
        l[i] = l[min_index]
        l[min_index] = temp
        
    return l

print(selection_sort([7,3,6,2,5,0]))  