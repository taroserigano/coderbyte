'''


Moving Median
HIDE QUESTION
Have the function MovingMedian(arr) read the array of numbers stored in arr which will contain a sliding window size, N, as the first element in the array and the rest will be a list of numbers. Your program should return the Moving Median for each element based on the element and its N-1 predecessors, where N is the sliding window size. The final output should be a string with the moving median corresponding to each entry in the original array separated by commas.

Note that for the first few elements (until the window size is reached), the median is computed on a smaller number of entries. For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] then your program should output "1,2,3,5,6,6,4,3"

Use the Parameter Testing feature in the box below to test your code with different arguments.

"[3, 1, 3, 5, 10, 6, 4, 3, 1]"

'''

from numpy import median
def MovingMedian(arr):
    N = arr[0]
    answer = ""
    for i in range(1, len(arr)):
        
        start = max(i+1-N, 1)
        end = i + 1
        a = arr[start:end]
        
        answer += "," + str(int(median(a)))
    return answer[1:]
print MovingMedian(raw_input())