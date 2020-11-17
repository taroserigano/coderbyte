'''


Max Subarray
Have the function MaxSubarray(arr) take the array of numbers stored in arr and determine the largest sum that can be formed by any contiguous subarray in the array. For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11 because the sum is formed by the subarray [5, -1, 7]. Adding any element before or after this subarray would make the sum smaller.
Examples
Input: [1, -2, 0, 3]
Output: 3
Input: [3, -1, -1, 4, 3, -1]
Output: 8

'''

def MaxSubarray(arr):

  # code goes here
  maxSubArray = arr[0]

  for i in range(0, len(arr)):
    for j in range(i+1, len(arr)+1):
      if sum(arr[i:j]) > maxSubArray:
        maxSubArray = sum(arr[i:j])
  return maxSubArray      




# keep this function call here 
print MaxSubarray(raw_input())