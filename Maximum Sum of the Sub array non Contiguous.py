#Time complexity O(n):
def nonContSubSum(arr):
    l = len(arr)
    s1 = arr[0]
    s2 = 0
    for i in range(1,l):
        s3 = max(s1,s2)
        s2 = s3
        s1 = s2+arr[i]
    return max(s1,s2)
print(nonContSubSum([1,2,-1,3,4,-5,20]))
