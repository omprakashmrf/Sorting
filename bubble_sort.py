a = [34,56,23,12,4,6,8,0,9]
def buble_sort(a):
    n = len(a)
    isswappwed = False
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                isswappwed = True
        if not isswappwed:
            break
    return a       
                
print(buble_sort(a))

if __name__ == '__main__':
    element  = ['fdgf', 'dghb', 'rtghg', 'rtthgbgn', 'hyhnhuy']
    buble_sort(element)
    print(element)
                
                


