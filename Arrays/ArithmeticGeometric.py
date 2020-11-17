'''
Arith Geo
Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.
Examples
Input: [5,10,15]
Output: Arithmetic
Input: [2,4,16,24]
Output: -1
'''


def ArithGeo(arr):

  # code goes here
  arith = arr[1] - arr[0]
  geome = arr[1] / arr[0]

  for i in range(2, len(arr)):

    if arr[i] - arr[i-1] != arith:
      arith = None

    if arr[i] / arr[i-1] != geome:
      geome = None 

    if arith == None and geome == None:
      return -1

  return 'Arithmetic' if arith != None else 'Geometric'

# keep this function call here 
print ArithGeo(raw_input([1,2,3,4]))