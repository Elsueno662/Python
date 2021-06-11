# Bubble Sort
def bubble_sort(lis):
    n = len(lis)
    for i in range(n-1):
        flag = True
        for j in range(0, n-i-1):
            if lis[j] > lis[j+1] :
                lis[j], lis[j+1] = lis[j+1], lis[j]
                flag = False
        if flag:
            break

    return lis


# Binary Search
def binary_search(lis, value):
    l_lim = 0
    u_lim = len(lis)-1
    mid = 0
 
    while l_lim <= u_lim:
 
        mid = (l_lim + u_lim)//2
 
        if lis[mid] < value:
            l_lim = mid + 1
 
        elif lis[mid] > value:
            u_lim = mid - 1
 
        else:
            return mid

    return -1


lis = [18,4,2,5,17,3,1]
sorted_lis = bubble_sort(lis)
result = binary_search(sorted_lis, 4)
 
if result != -1:
    print(f"Element is present at index {str(result)} in the sorted list")
    print(f"The sorted list is: {sorted_lis}")
else:
    print("Element is not present in the list")
