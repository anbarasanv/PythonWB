#Quick Sort: Time complexity := O(n log n) - Average case
#Hence its inplace sort, the Space complexity: O(1)
'''
Logic: (Divide and conquer) 
step 0: follow the below steps in to the "Quick_Sort" function
step 1: Need to choose a pivot element ( Here it last element of the list )
step 2: find the partition Index. ( Which means arrange pivot element to the correct poisition
        Here this will be handled by "Partition" function
step 3: divide the list by two => left_list <pivot> right_list
step 4: now recursively call the "Quick_Sort" function


'''
import  timeit
start = timeit.timeit()
def Quick_Sort(A,begin,end):
    '''Recursively sort the elements'''
    if begin < end:
         #To make the Quick_Sort random, will reduce the time complexity for sorted list
        A[begin],A[end] = A[end],A[begin] 
        
        partition_index = Partition(A,begin,end)
        Quick_Sort(A,begin,partition_index-1)
        Quick_Sort(A,partition_index+1,end)


def Partition(A,begin,end):
    '''This function computes the partition_index'''
    pivot = A[end]
    partition_index = begin
    for i in range(begin,end):
        if(A[i] <= pivot):
            #When A[i] less then pivot swap hppends
            A[i],A[partition_index] = A[partition_index],A[i]
            partition_index +=1
    #Final swap for arrange the piovot to correct poisition
    A[partition_index],A[end] = A[end], A[partition_index]
    return partition_index
    
    
A = [7,6,5,4,3,2,1,0]
begin = 0
end = len(A)-1
Quick_Sort(A,begin,end)
print(A)
stop = timeit.timeit()

print("Time taken:",start - stop)

#With randomized Time taken: -0.0014381029977812432
#Without randomized Time taken: 4.344100034359144e-05
