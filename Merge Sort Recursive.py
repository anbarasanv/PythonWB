#Time complexity O(n log n)
def merge(left,right):
    '''This Function will merge 2 array or list'''
    result = []
    i,j = 0,0
    #Comparing two list for smallest element
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    #left elements appends to the result list
    result += left[i:]
    result += right[j:]
    return result

def mergeSort(lst):
    '''This is the recursive sorting array'''
    if(len(lst) <= 1):
        return lst
    #Finding the mid
    mid = int(len(lst)/2)
    #Recursive call for left and right array or list
    left  = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    #Merginging splited lists or array
    return merge(left,right)

A = [1,-2,0,-3,10,999999,20]

print(mergeSort(A))
    

    
