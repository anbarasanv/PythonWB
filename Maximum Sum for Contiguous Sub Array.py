#Time complexity: O(n)
import sys
def maxSumSubarray(arr):
    '''This function returns the maximum sum of contiguous sub array'''
    #Here finalMax declared to hold both positive and negative integers.
    #So that the array contains negative integers max sum also canbe computed
    finalMax,tempMax = -sys.maxsize ,0
    for i in range(len(arr)):
        tempMax = tempMax+arr[i]
        print('tempMax:',tempMax)
        if tempMax > finalMax:
            print('finalMax:',finalMax)
            finalMax = tempMax
        if tempMax < 0:
            tempMax = 0
    return finalMax
testArray = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
#testArray = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSumSubarray(testArray))
