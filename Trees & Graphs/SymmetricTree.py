'''



Symmetric Tree
HIDE QUESTION
Have the function SymmetricTree(strArr) take the array of strings stored in strArr, which will represent a binary tree, and determine if the tree is symmetric (a mirror image of itself). The array will be implemented similar to how a binary heap is implemented, except the tree may not be complete and NULL nodes on any level of the tree will be represented with a #. For example: if strArr is ["1", "2", "2", "3", "#", "#", "3"] then this tree looks like the following:



For the input above, your program should return the string true because the binary tree is symmetric.

Use the Parameter Testing feature in the box below to test your code with different arguments.


"["1", "2", "2", "3", "#", "#", "3"]"



'''



def SymmetricTree(a):

  # code goes here
  arr, branch, store = list(a), 1, []

  while len(arr) > 0: #squeeze out
    x = []
    for i in range(branch):
      x.append(arr[0])
      del arr[0]
    store.append(x)
    branch *= 2
  for i in store:

    if i != list(reversed(i)) :
      return 'false'
  return 'true'       
      



# keep this function call here 
print SymmetricTree(raw_input())